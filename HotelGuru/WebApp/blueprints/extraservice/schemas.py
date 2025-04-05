from marshmallow import Schema, fields, validate
from WebApp.models.extraservice import ExtraService
import WebApp.blueprints.reservation.schemas as ReservationRequestSchemas

class ExtraServiceListSchema(Schema):
    id = fields.Integer(dump_only=True)
    reservation_id = fields.Integer(required=True)
    service_id = fields.Integer(required=True)
    quantity = fields.Integer(
        required=True,
        validate=validate.Range(min=1, error="Quantity must be at least 1")
    )
    
    #Relationships - can be expanded with nested schemas if needed
    #reservation = fields.Nested(ReservationRequestSchemas, only=('id',), dump_only=True)
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
    quantity = fields.Integer(
        required=True,
        validate=validate.Range(min=1, error="Quantity must be at least 1")
    )

