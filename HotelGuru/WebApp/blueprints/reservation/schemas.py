from marshmallow import Schema, fields, validate, post_dump
from WebApp.blueprints.rooms.schemas import RoomsListSchema
from WebApp.models.rooms import Rooms
from WebApp.models.extraservice import ExtraService
from WebApp.models.extraservice_order import ExtraServiceOrder
from WebApp.extensions import db
from sqlalchemy import select

class BaseRoomSchema(Schema):   #ezzzel tudom megkapni a statusz enumot
    status = fields.Method("get_status")
    type = fields.Method("get_type")

    def get_status(self, obj):
        return obj.status.value

    def get_type(self, obj):
        return obj.type.value
    
class ReservationUpdateSchema(Schema):
    check_in = fields.Date(required=True)
    check_out = fields.Date(required=True)

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
    status = fields.String()
    items = fields.Method("get_items")
    extraservices = fields.Method("get_extraservices")

    def get_items(self, obj):
            return RoomsListSchema(many=True).dump(obj.items or [])

    def get_extraservices(self, obj):
        orders = db.session.execute(
            db.select(ExtraServiceOrder).where(ExtraServiceOrder.reservation_id == obj.id)
        ).scalars().all()

        results = []
        for order in orders:
            service = db.session.get(ExtraService, order.extraservice_id)
            if service:
                results.append({
                    "name": service.name,
                    "quantity": order.quantity,
                    "price": service.price
                })
        return results
    


        

class ReservationRequestSchema(Schema):
    user_id = fields.Integer(required=True)
    check_in = fields.Date(required=True)
    check_out = fields.Date(required=True)
    items = fields.List(fields.Dict(keys=fields.String(), values=fields.Raw()), required=True)