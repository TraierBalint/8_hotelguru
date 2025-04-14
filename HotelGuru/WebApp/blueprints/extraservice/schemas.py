from marshmallow import Schema, fields, validate
from WebApp.blueprints.reservation.schemas import ReservationResponseSchema

class ExtraServiceResponseSchema(Schema):
    id = fields.Integer()
    name = fields.String(required=True)
    price = fields.Float(required=True)
    reservation_id = fields.Integer()


class ExtraServiceRequestSchema(Schema):

    name = fields.String(required=True)
    price = fields.Float(required=True)
    reservation_id = fields.Integer(required=True)


