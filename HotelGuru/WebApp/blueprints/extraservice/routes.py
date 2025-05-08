from flask import jsonify
from WebApp.blueprints.extraservice import bp
from WebApp.blueprints.extraservice.schemas import ExtraServiceRequestSchema, ExtraServiceResponseSchema,ExtraServiceListResponseSchema
from WebApp.blueprints.extraservice.service import ExtraServiceService
from apiflask import HTTPError
from WebApp.extensions import auth
from WebApp.blueprints import role_required


@bp.route('/')
def index():
    return 'This is the ExtraService Blueprint'


@bp.get('/list')
@bp.doc(tags=["extraservice"])
@bp.output(ExtraServiceListResponseSchema(many=True))
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


@bp.post("/order/add")
@bp.input(ExtraServiceRequestSchema, location="json")
@bp.auth_required(auth)
@role_required(["User", "Receptionist", "Administrator"])
def add_extra_service(json_data):
    success, response = ExtraServiceService.create(json_data)
    if success:
        return {"message": response}, 201
    raise HTTPError(message=response, status_code=400)


@bp.put('/update/<int:service_id>')
@bp.doc(tags=["extraservice"])
@bp.input(ExtraServiceRequestSchema, location="json")
@bp.output(ExtraServiceResponseSchema)
@bp.auth_required(auth)
@role_required(["Administrator","Receptionist"])
def update_service(service_id, json_data):
    success, response = ExtraServiceService.update(service_id, json_data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)


@bp.delete('/delete/<int:service_id>')
@bp.doc(tags=["extraservice"])
@bp.auth_required(auth)
@role_required(["Administrator","Receptionist"])
def delete_service(service_id):
    success, response = ExtraServiceService.delete(service_id)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.post('/create')
@bp.doc(tags=["extraservice"])
@bp.input(ExtraServiceRequestSchema, location="json")  
@bp.output(ExtraServiceResponseSchema)
@bp.auth_required(auth)
@role_required(["Administrator","Receptionist"])

def create_service(json_data):
    success, response = ExtraServiceService.create(json_data)
    if success:
        return response, 201
    raise HTTPError(message=response, status_code=400)