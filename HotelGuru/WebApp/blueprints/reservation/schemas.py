from marshmallow import Schema, fields
from WebApp.blueprints.user.schemas import AddressSchema

class ReservationItemSchema(Schema):
    
    room_id = fields.Integer()
    quantity = fields.Integer()  # és ez se biztos hogy jó class

class ReservationRequestSchema(Schema):
    
    user_id=fields.Integer()
    address_id = fields.Integer()

    
class ReservationResponseSchema(Schema):
    id = fields.Integer()
    user_id = fields.Integer()
    address=fields.Nested(AddressSchema)