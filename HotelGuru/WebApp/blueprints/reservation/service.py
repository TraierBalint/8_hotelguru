from WebApp.models.reservation import Reservation
from WebApp.models.reservation_rooms import ReservationRoom
from WebApp.models.rooms import Rooms
from WebApp.extensions import db
from WebApp.blueprints.reservation.schemas import ReservationResponseSchema, ReservationRequestSchema
from WebApp.blueprints.rooms.schemas import RoomsListSchema
from sqlalchemy import select
from datetime import datetime
from apiflask import APIBlueprint, HTTPError
from flask import request
from sqlalchemy import select, and_
from marshmallow import post_dump





class ReservationService:

    @staticmethod
    def get_rooms_for_reservation(reservation_id):
        try:
            room_ids = db.session.query(ReservationRoom.room_id).filter_by(reservation_id=reservation_id).all()
            room_ids = [r[0] for r in room_ids]
            rooms = db.session.execute(select(Rooms).where(Rooms.id.in_(room_ids))).scalars().all()
            return True, rooms
        except Exception as ex:
            return False, str(ex)

    @staticmethod
    def reservation_add(request_data):
        try:
            check_in = request_data["check_in"]
            check_out = request_data["check_out"]

            items = request_data.pop("items", [])
            for item in items:     #ez a rész nézzi meg hogy a szobák foglaltak e
                room_id = item["room_id"]
                conflict = db.session.execute(
                    select(ReservationRoom)
                    .join(Reservation)
                    .filter(
                        ReservationRoom.room_id == room_id,
                        Reservation.check_out > check_in,
                        Reservation.check_in < check_out
                    )
                ).scalars().all()

                if conflict:
                    return False, f"A szoba (id: {room_id}) már foglalt a megadott időszakban!"
            reservation = Reservation(**request_data)
            db.session.add(reservation)
            db.session.flush()

            for item in items:
                rr = ReservationRoom(reservation_id=reservation.id, room_id=item["room_id"])
                db.session.add(rr)

            db.session.commit()
            reservation.items = ReservationService.get_rooms_for_reservation(reservation.id)
            return True, reservation

        except Exception as ex:
            db.session.rollback()
            return False, str(ex)
        
    @staticmethod
    def reservation_update(rid, request_data):
        try:
            print("check_in type:", type(request_data["check_in"]))
            reservation = db.session.get(Reservation, rid)
            if not reservation:
                return False, "Reservation not found"

            difference = (reservation.check_in - datetime.today().date()).days

            if difference < 0:
                return False, 
            if difference > 7:
                return False,

            reservation.check_in = request_data["check_in"]
            reservation.check_out = request_data["check_out"]
            db.session.commit()
            reservation.items = ReservationService.get_rooms_for_reservation(reservation.id)
            return True, ReservationResponseSchema().dump(reservation)

        except Exception as ex:
            db.session.rollback()
            return False, str(ex)

    @staticmethod
    def reservation_delete(rid):
        try:
            reservation = db.session.get(Reservation, rid)
            if not reservation:
                return False, "Reservation not found"

            db.session.delete(reservation)
            db.session.commit()
            return True, "Reservation deleted successfully"

        except Exception as ex:
            db.session.rollback()
            return False, str(ex)

    @staticmethod
    def reservation_list_all():
        reservations = db.session.execute(
            select(Reservation).order_by(Reservation.check_in.asc())
        ).scalars().all()
        for r in reservations:
            r.items = ReservationService.get_rooms_for_reservation(r.id)
        return True, reservations

    @staticmethod
    def reservation_list_by_user(user_id):
        reservations = db.session.execute(
            select(Reservation).filter_by(user_id=user_id)
        ).scalars().all()
        for r in reservations:
            r.items = ReservationService.get_rooms_for_reservation(r.id)
        return True, ReservationResponseSchema(many=True).dump(reservations)

    @staticmethod
    def reservation_get_by_id(rid):
        reservation = db.session.get(Reservation, rid)
        if reservation is None:
            return False, "Reservation not found"
        reservation.items = ReservationService.get_rooms_for_reservation(reservation.id)
        return True, ReservationResponseSchema().dump(reservation)

