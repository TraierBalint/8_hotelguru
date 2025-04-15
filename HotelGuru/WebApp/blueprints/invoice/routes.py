from flask import jsonify
from apiflask import HTTPError
from WebApp.blueprints.invoice import bp
from WebApp.blueprints.invoice.schemas import InvoiceRequestSchema, InvoiceResponseSchema
from WebApp.blueprints.invoice.service import InvoiceService

@bp.route('/')
def index():
    return 'This is the Invoice Blueprint'


@bp.post('/create')
@bp.input(InvoiceRequestSchema, location='json')
@bp.output(InvoiceResponseSchema)
def create_invoice(json_data):
    success, response = InvoiceService.create(json_data)
    if success:
        return response, 201
    raise HTTPError(message=response, status_code=400)