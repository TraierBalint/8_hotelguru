from WebApp.blueprints.rooms.schemas import RoomsResponseSchema, RoomsListSchema
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
            return False, str(ex)#"room_add() error!"
        return True, RoomsResponseSchema().dump(room)
    
    @staticmethod # Szoba frisítése id alapján
    # ezt az egészet a rooms/routes.py-ban hívjuk meg a room_update() függvényben
    def room_update(rid, request):
        try:
            room = db.session.get(Rooms, rid)
            if room:
                room.number = int(request["number"])
                room.type = request["type"]
                room.status = request["status"]
                room.price = float(request["price"])
                db.session.commit()
            
        except Exception as ex:
            return False, "room_update() error!"
        return True, RoomsResponseSchema().dump(room)
 

    @staticmethod # Szoba listázása típusa alapján
    # ezt az egészet a rooms/routes.py-ban hívjuk meg a room_list_type() függvényben
    def room_list_type(type_name):
        if type_name is None:
            rooms = db.session.execute(select(Rooms).filter(Rooms.deleted.is_(0))).scalars()
        else:
            rooms = db.session.execute(
                select(Rooms).filter(
                    Rooms.deleted.is_(0),
                    Rooms.type == type_name
                )).scalars()

        return True, RoomsListSchema().dump(rooms, many=True)