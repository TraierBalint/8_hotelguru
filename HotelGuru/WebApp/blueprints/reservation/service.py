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
    
    @staticmethod #a foglalásban  módosítunk
    # ezt az egészet a reservation/routes.py-ban hívjuk meg a reservation_update() függvényben
    def reservation_update(rid, request):
        diffference = (datetime.today().strftime('%Y-%m-%d') - reservation.check_in).days   #kiszámitja a két dátum közötti különbséget     
        try:
            reservation = db.session.get(Reservation, rid)
            if reservation:
                reservation.check_in = request["start_date"]
                reservation.check_out = request["end_date"]
                reservation.room_id = request["room_id"]
                
                db.session.commit()

            elif diffference > 7: # 7 napnál régebbi foglalásokat nem lehet törölni
                return False, "Reservation cannot be canceld cause beyond 1 weeks to check in!"
        except Exception as ex:
            return False, "reservation_update() error!"
        return True, ReservationResponseSchema().dump(reservation)
    
    @staticmethod  
    def reservation_delete(rid): # foglalás törlés
    # ezt az egészet a reservation/routes.py-ban hívjuk meg a reservation_delete() függvényben
        try:
            reservation = db.session.get(Reservation, rid)
            if reservation:
                reservation.deleted = 1
                db.session.commit()
        except Exception as ex:
            return False, "reservation_delete() error!"
        return True, "OK"
    
    