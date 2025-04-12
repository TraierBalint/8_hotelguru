from marshmallow import Schema, fields, validate, post_dump
from WebApp.blueprints.rooms.schemas import RoomsListSchema
from WebApp.models.rooms import Rooms
from WebApp.extensions import db
from sqlalchemy import select

class BaseRoomSchema(Schema):   #ezzzel tudom megkapni a statusz enumot
    status = fields.Method("get_status")
    type = fields.Method("get_type")

    def get_status(self, obj):
        return obj.status.value

    def get_type(self, obj):
        return obj.type.value

class RoomsListSchema(BaseRoomSchema):
    id = fields.Integer()
    name = fields.String()
    price = fields.Float()

class RoomsResponseSchema(BaseRoomSchema):
    name = fields.String()
    price = fields.Float()

class RoomsRequestSchema(Schema):
    name = fields.String()
    type = fields.String(required=True, validate=validate.OneOf(["single", "double", "suite"]))
    status = fields.String(required=True, validate=validate.OneOf(["available", "reserved", "maintenance"]))
    price = fields.Float()

class ReservationResponseSchema(Schema):
    id = fields.Integer()
    user_id = fields.Integer()
    check_in = fields.Date()
    check_out = fields.Date()
    items = fields.Method("get_items")

    def get_items(self, obj):
        #lekérdezi a foglalt szobákat a reservation_rooms táblából , lekérdezi az adatbázisból és visszaadja Jsonben
        room_ids = [rr.room_id for rr in obj.reservation_rooms]
        rooms = db.session.execute(select(Rooms).where(Rooms.id.in_(room_ids))).scalars().all()
        return RoomsListSchema(many=True).dump(rooms)

    

class ReservationRequestSchema(Schema):
    user_id = fields.Integer(required=True)
    check_in = fields.Date(required=True)
    check_out = fields.Date(required=True)
    items = fields.List(fields.Dict(keys=fields.String(), values=fields.Raw()), required=True)