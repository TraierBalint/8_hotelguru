from marshmallow import Schema, fields, validate
from WebApp.blueprints.reservation.schemas import ReservationResponseSchema

class ExtraServiceResponseSchema(Schema):
    extraservice_id = fields.Integer(required=True)
    reservation_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True)

class ExtraServiceListResponseSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    price = fields.Float(required=True)

class ExtraServiceRequestSchema(Schema):

    extraservice_id = fields.Integer(required=True)
    reservation_id = fields.Integer(required=True)
    quantity = fields.Integer(required=True)