from marshmallow import Schema, fields


class RoomsListSchema(Schema):
    id = fields.Integer()
    number = fields.Integer()
    type = fields.String()
    price = fields.Float()
    status = fields.String(default="available")
    
class RoomsResponseSchema(Schema):
    number = fields.Integer()
    type = fields.String()
    status = fields.String()
    price = fields.Float()


   