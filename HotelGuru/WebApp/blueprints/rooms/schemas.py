from marshmallow import Schema, fields


class RoomsListSchema(Schema):
    id = fields.Integer()
    #number = fields.Integer() jelenleg nem jó mert az adatmodellben ez string
    number = fields.String()
    
    type = fields.String()
    price = fields.Float()
    status = fields.String(default="available")
    
class RoomsResponseSchema(Schema):
    #number = fields.Integer()
    number = fields.String()
    type = fields.String()
    status = fields.String()
    price = fields.Float()


class RoomsRequestSchema(Schema):
    #number = fields.Integer()
    number = fields.String()
    type = fields.String()
    status = fields.String()
    price = fields.Float()

   