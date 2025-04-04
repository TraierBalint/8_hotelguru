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
    
    @staticmethod #Szoba törlés
    # ezt az egészet a rooms/routes.py-ban hívjuk meg a room_delete() függvényben
    def room_delete(rid):
        try:
            room = db.session.get(Rooms, rid)
            if room:
                room.deleted = 1
                db.session.commit()
            
        except Exception as ex:
            return False, "room_update() error!"
        return True, "OK"
    
    @staticmethod  # Szoba hozzáadás
    # ezt az egészet a rooms/routes.py-ban hívjuk meg a room_add_new() függvényben
    def room_add(request):
        try:
        
            room = Rooms(**request)
            db.session.add(room)
            db.session.commit()
            
        except Exception as ex:
            return False, "room_add() error!"
        return True, RoomsResponseSchema().dump(room)
    

    