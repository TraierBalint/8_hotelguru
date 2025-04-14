from marshmallow import Schema, fields, validate
from WebApp.blueprints.reservation.schemas import ReservationResponseSchema

class ExtraServiceListSchema(Schema):
    id = fields.Integer()
    reservation_id = fields.Integer()
    service_id = fields.Integer()
    quantity = fields.Integer()
    reservation = fields.Nested(ReservationResponseSchema, only=('id',), dump_only=True)
    #service = fields.Nested('ServiceSchema', only=('id', 'name'), dump_only=True)

class ExtraServiceResponseSchema(Schema):
    id = fields.Integer()
    reservation_id = fields.Integer()
    service_id = fields.Integer()
    quantity = fields.Integer()
    #service = fields.Nested(ServiceSchema, only=('id', 'name'))

class ExtraServiceRequestSchema(Schema):
    reservation_id = fields.Integer(required=True)
    service_id = fields.Integer(required=True)
    quantity = fields.Integer()

