from marshmallow import Schema, fields

class InvoiceRequestSchema(Schema):
    reservation_id = fields.Integer(required=True)
    issue_date = fields.Date(required=True)


class InvoiceResponseSchema(Schema):
    id = fields.Integer()
    reservation_id = fields.Integer()
    issue_date = fields.Date()
    total_amount = fields.Float()