from WebApp.blueprints.rooms.schemas import RoomsResponseSchema, RoomsListSchema
from WebApp.extensions import db
from WebApp.models.rooms import Rooms ,RoomStatus, RoomType
from sqlalchemy import select
from flask import Flask, jsonify

class RoomsService:

    @staticmethod   # Ki listázas az összes szobát, amelyik szobát nem töröltünk ki 
    # ezt az egészet a rooms/routes.py-ban hívjuk meg a rooms_list_all() függvényben
    def rooms_list_all():
        #rooms = db.session.execute( select(Rooms).filter(Rooms.deleted.is_(0))).scalars()
        #return True, RoomsListSchema.dump(rooms, many=True) 
        #return True, rooms  #itt nem dump-olom ki a roomot,mert routes.py-ban már ki van dump-olva a room
        rooms = db.session.query(Rooms).all()
        return True, jsonify([room.to_dict() for room in rooms])
    
    
    @staticmethod #Szoba törlés
    # ezt az egészet a rooms/routes.py-ban hívjuk meg a room_delete() függvényben
    def room_delete(rid):
        try:
            room = db.session.get(Rooms, rid)
            if room:
                db.session.delete(room)  # végleges törlés
                db.session.commit()
                return True, "Szoba véglegesen törölve."
            return False, "Szoba nem található."
        except Exception as ex:
            db.session.rollback()
            return False, f"room_delete() hiba: {ex}"
    
    @staticmethod  # Szoba hozzáadás
    # ezt az egészet a rooms/routes.py-ban hívjuk meg a room_add_new() függvényben
    def room_add(request):
        try:
            request["status"] = RoomStatus(request["status"]) 
            request["type"] = RoomType(request["type"])
        
            rooms = Rooms(**request)
            db.session.add(rooms)
            db.session.commit()
            
        except Exception as ex:
            return False, str(ex)#"room_add() error!"
        return True, jsonify(rooms.to_dict())  # itt nem dump-olom ki a roomot,mert routes.py-ban már ki van dump-olva a room
    
    @staticmethod # Szoba frisítése id alapján
    # ezt az egészet a rooms/routes.py-ban hívjuk meg a room_update() függvényben
    def room_update(rid, request):
        try:
            request["status"] = RoomStatus(request["status"]) 
            request["type"] = RoomType(request["type"])
            rooms = db.session.get(Rooms, rid)
            if rooms:
                rooms.name = str(request["name"])
                rooms.type = request["type"]
                rooms.status = request["status"]
                rooms.price = float(request["price"])
                db.session.commit()
            
        except Exception as ex:
            return False, "room_update() error!"
        return True, jsonify([room.to_dict() for room in rooms])
 

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