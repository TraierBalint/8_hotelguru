from WebApp.extensions import db
from WebApp.blueprints.reservation.schemas import ReservationResponseSchema, ReservationRequestSchema, ReservationItemSchema
from datetime import datetime
from WebApp.models.reservation import Reservation

from sqlalchemy import select, and_



class ReservationService:
    

    @staticmethod  #foglalás hozzáadása
    def reservation_add(request): 
        try:
            reservation = Reservation(**request)
            db.session.add(reservation)
            db.session.commit()
        except Exception as ex:
            return False, "reservation_add() error!"
        return True, ReservationResponseSchema().dump(reservation)
    
    