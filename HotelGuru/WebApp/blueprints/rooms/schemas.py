from marshmallow import Schema, fields


class RoomsListSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    price = fields.Float()
    status = fields.String(default="available")
    type = fields.String()
    
class RoomsResponseSchema(Schema):
    
    name = fields.String()
    price = fields.Float()
    status = fields.String()
    type = fields.String()


class RoomsRequestSchema(Schema):
    
    name = fields.String()
    type = fields.String()
    status = fields.String()
    price = fields.Float()

   