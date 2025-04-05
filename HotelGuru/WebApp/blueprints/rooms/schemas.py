from marshmallow import Schema, fields


class RoomsListSchema(Schema):
    id = fields.Integer()
    name = fields.String()
    
    type = fields.String()
    price = fields.Float()
    status = fields.String(default="available")
    
class RoomsResponseSchema(Schema):
    
    name = fields.String()
    type = fields.String()
    status = fields.String()
    price = fields.Float()


class RoomsRequestSchema(Schema):
    
    name = fields.String()
    type = fields.String()
    status = fields.String()
    price = fields.Float()

   