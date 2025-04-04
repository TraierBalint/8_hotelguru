from WebApp.blueprints.rooms.schemas import RoomsResponseSchema
from WebApp.extensions import db
from WebApp.models.rooms import Rooms
from sqlalchemy import select

class RoomsService:

    @staticmethod   # Ki listázas az összes szobát, amelyik szobát nem töröltünk ki 
    # ezt az egészet a rooms/routes.py-ban hívjuk meg a rooms_list_all() függvényben
    def rooms_list_all():
        rooms = db.session.execute( select(Rooms).filter(Rooms.deleted.is_(0))).scalars()
        return True, RoomsResponseSchema().dump(rooms, many = True) 
    

    