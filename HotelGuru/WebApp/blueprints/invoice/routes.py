from flask import jsonify
from apiflask import HTTPError
from WebApp.blueprints.invoice import bp
from WebApp.blueprints.invoice.schemas import InvoiceRequestSchema, InvoiceResponseSchema ,InvoiceUpdateSchema
from WebApp.blueprints.invoice.service import InvoiceService
from WebApp.extensions import auth
from WebApp.blueprints import role_required

@bp.route('/')
def index():
    return 'This is the Invoice Blueprint'


@bp.post('/create')
@bp.input(InvoiceRequestSchema, location='json')
@bp.output(InvoiceResponseSchema)
@bp.auth_required(auth)
@role_required(["Administrator","Receptionist"])  
def create_invoice(json_data):
    success, response = InvoiceService.create(json_data)
    if success:
        return response, 201
    raise HTTPError(message=response, status_code=400)


@bp.get("/<int:invoice_id>")
@bp.doc(tags=["invoice"])
@bp.output(InvoiceResponseSchema)
@bp.auth_required(auth)
@role_required(["Administrator","Receptionist"])
def get_invoice(invoice_id):
    success, response = InvoiceService.get_by_id(invoice_id)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=404)

@bp.get("/list")
@bp.doc(tags=["invoice"])
@bp.output(InvoiceResponseSchema(many=True))
@bp.auth_required(auth)
@role_required(["Administrator","Receptionist"])
def list_invoices():
    success, response = InvoiceService.list_all()
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.put('/update/<int:invoice_id>')
@bp.doc(tags=["invoice"])
@bp.input(InvoiceUpdateSchema, location="json")
@bp.output(InvoiceResponseSchema)
@bp.auth_required(auth)
@role_required(["Administrator","Receptionist"])
def update_invoice(invoice_id, json_data):
    success, response = InvoiceService.update(invoice_id, json_data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.delete("/delete/<int:invoice_id>")
@bp.doc(summary="Delete invoice", description="Deletes an invoice by ID", tags=["invoice"])
@bp.auth_required(auth)
@role_required(["Administrator","Receptionist"])
def delete_invoice(invoice_id):
    success, response = InvoiceService.delete(invoice_id)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)