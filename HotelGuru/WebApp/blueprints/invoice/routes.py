from flask import jsonify
from apiflask import HTTPError
from WebApp.blueprints.invoice import bp
from WebApp.blueprints.invoice.schemas import InvoiceRequestSchema, InvoiceResponseSchema ,InvoiceUpdateSchema
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


@bp.get("/<int:invoice_id>")
@bp.doc(tags=["invoice"])
@bp.output(InvoiceResponseSchema)
def get_invoice(invoice_id):
    success, response = InvoiceService.get_by_id(invoice_id)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=404)

@bp.get("/list")
@bp.doc(tags=["invoice"])
@bp.output(InvoiceResponseSchema(many=True))
def list_invoices():
    success, response = InvoiceService.list_all()
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.put('/<int:invoice_id>')
@bp.doc(tags=["invoice"])
@bp.input(InvoiceUpdateSchema, location="json")
@bp.output(InvoiceResponseSchema)
def update_invoice(invoice_id, json_data):
    success, response = InvoiceService.update(invoice_id, json_data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)