from marshmallow import Schema, fields
from WebApp.blueprints.user.schemas import AddressSchema

class ReservationItemSchema(Schema):
    
    room_id = fields.Integer()
    

class ReservationRequestSchema(Schema):
    
    user_id=fields.Integer()
    address_id = fields.Integer()
    check_in = fields.Date()
    check_out = fields.Date()
    items = fields.Nested(ReservationItemSchema, many=True)

    
class ReservationResponseSchema(Schema):
    id = fields.Integer()
    user_id = fields.Integer()
    address=fields.Nested(AddressSchema)
    check_in = fields.Date()
    check_out = fields.Date()
    items = fields.Nested(ReservationItemSchema, many=True)