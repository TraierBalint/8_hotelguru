from marshmallow import Schema, fields

class ReservationItemSchema(Schema):
    
    room_id = fields.Integer()
    quantity = fields.Integer()  # és ez se biztos hogy jó class

class ReservationRequestSchema(Schema):
    
    id = fields.Integer()
    guest_id = fields.Integer()
    room_id = fields.Integer()
    check_in = fields.DateTime()
    check_out = fields.DateTime()
    items = fields.Nested(ReservationItemSchema(many=True)) # nem biztos hogy ez ide kell ,mert csak sejtésem van ,hogy ez megszámolja 
    #a szoba foglalásokat, de nem biztos hogy ez a helyes megoldás
    confirmed = fields.Boolean()
    total_price = fields.Float()
    
    
    
class ReservationResponseSchema(Schema):
    id = fields.Integer()
    guest_id = fields.Integer()
    room_id = fields.Integer()
    check_in = fields.DateTime()
    check_out = fields.DateTime()
    items = fields.Nested(ReservationItemSchema(many=True)) # szintúgy nem biztos hogy jó
    confirmed = fields.Boolean()
    total_price = fields.Float()