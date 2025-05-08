from marshmallow import Schema, fields,validate


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
    status = fields.Method("get_status")  
    type = fields.Method("get_type")      

    
    
class RoomsResponseSchema(BaseRoomSchema):
    
    name = fields.String()
    price = fields.Float()
    


class RoomsRequestSchema(Schema):
    
    name = fields.String()
    type = fields.String(required=True, validate=validate.OneOf(["single", "double", "suite"]))
    status = fields.String(required=True, validate=validate.OneOf(["available", "reserved", "maintenance"]))
    price = fields.Float()

   