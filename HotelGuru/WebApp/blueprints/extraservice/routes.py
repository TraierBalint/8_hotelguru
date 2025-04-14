from flask import jsonify
from WebApp.blueprints.extraservice import bp
from WebApp.blueprints.extraservice.schemas import ExtraServiceRequestSchema, ExtraServiceResponseSchema
from WebApp.blueprints.extraservice.service import ExtraServiceService
from apiflask import HTTPError


@bp.route('/')
def index():
    return 'This is the ExtraService Blueprint'


@bp.get('/list')
@bp.doc(tags=["extraservice"])
@bp.output(ExtraServiceResponseSchema(many=True))
def list_services():
    success, response = ExtraServiceService.get_all()
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)


@bp.get('/<int:service_id>')
@bp.doc(tags=["extraservice"])
@bp.output(ExtraServiceResponseSchema)
def get_service(service_id):
    success, response = ExtraServiceService.get_by_id(service_id)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=404)


@bp.post('/create')
@bp.doc(tags=["extraservice"])
@bp.input(ExtraServiceRequestSchema, location="json")
@bp.output(ExtraServiceResponseSchema)
def create_service(json_data):
    success, response = ExtraServiceService.create(json_data)
    if success:
        return response, 201
    raise HTTPError(message=response, status_code=400)


@bp.put('/update/<int:service_id>')
@bp.doc(tags=["extraservice"])
@bp.input(ExtraServiceRequestSchema, location="json")
@bp.output(ExtraServiceResponseSchema)
def update_service(service_id, json_data):
    success, response = ExtraServiceService.update(service_id, json_data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)


@bp.delete('/delete/<int:service_id>')
@bp.doc(tags=["extraservice"])
def delete_service(service_id):
    success, response = ExtraServiceService.delete(service_id)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)