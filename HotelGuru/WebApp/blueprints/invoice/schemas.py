from marshmallow import Schema, fields

class InvoiceRequestSchema(Schema):
    reservation_id = fields.Integer(required=True)
    issue_date = fields.Date(required=True)

class InvoiceItemSchema(Schema):
    id = fields.Integer()
    item_type = fields.String()
    item_id = fields.Integer()
    name = fields.String()
    price = fields.Float()
    quantity = fields.Integer()

class InvoiceResponseSchema(Schema):
    id = fields.Integer()
    reservation_id = fields.Integer()
    issue_date = fields.Date()
    total_amount = fields.Float()
    items = fields.List(fields.Nested(InvoiceItemSchema))

class InvoiceUpdateSchema(Schema):
    total_amount = fields.Float()
    issue_date = fields.Date()