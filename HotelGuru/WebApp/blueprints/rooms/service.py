from WebApp.blueprints.rooms.schemas import RoomsResponseSchema, RoomsListSchema
from WebApp.extensions import db
from WebApp.models.rooms import Rooms ,RoomStatus, RoomType
from sqlalchemy import select

class RoomsService:

 

    @staticmethod   # Ki listázas az összes szobát, amelyik szobát nem töröltünk ki 
    # ezt az egészet a rooms/routes.py-ban hívjuk meg a rooms_list_all() függvényben
    def rooms_list_all():
        rooms = db.session.execute( select(Rooms).filter(Rooms.deleted.is_(0))).scalars()
        return True, rooms #RoomsListSchema().dump(rooms, many=True) #itt nem dump-olom ki a roomot,mert routes.py-ban már ki van dump-olva a room
    
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
            request["status"] = RoomStatus(request["status"]) 
            request["type"] = RoomType(request["type"])
        
            room = Rooms(**request)
            db.session.add(room)
            db.session.commit()
            
        except Exception as ex:
            return False, str(ex)#"room_add() error!"
        return True, room  # itt nem dump-olom ki a roomot,mert routes.py-ban már ki van dump-olva a room
    
    @staticmethod # Szoba frisítése id alapján
    # ezt az egészet a rooms/routes.py-ban hívjuk meg a room_update() függvényben
    def room_update(rid, request):
        try:
            request["status"] = RoomStatus(request["status"]) 
            request["type"] = RoomType(request["type"])
            room = db.session.get(Rooms, rid)
            if room:
                room.name = str(request["name"])
                room.type = request["type"]
                room.status = request["status"]
                room.price = float(request["price"])
                db.session.commit()
            
        except Exception as ex:
            return False, "room_update() error!"
        return True, room
 

    @staticmethod # Szoba listázása típusa alapján
    # ezt az egészet a rooms/routes.py-ban hívjuk meg a room_list_type() függvényben
    def room_list_type(type_name):
        if type_name is None:
            rooms = db.session.execute(
                select(Rooms).filter(Rooms.deleted.is_(0))
            ).scalars().all()
        else:
            try:
                room_type_enum = RoomType(type_name)  # Enum típusúvá alakítjuk a type_name-t
            except ValueError:
                return False, f"Invalid room type: {type_name}"

            rooms = db.session.execute(
                select(Rooms).filter(
                    Rooms.deleted.is_(0),
                    Rooms.type == room_type_enum
                )
            ).scalars().all()

        return True, rooms

    
    @staticmethod  # Szoba listázása id alapján
    # ezt az egészet a rooms/routes.py-ban hívjuk meg a room_get_by_id() függvényben
    def room_get_by_id(rid):
        room = db.session.get(Rooms, rid)
        if not room or room.deleted:
            return False, "Room not found"
        return True, room