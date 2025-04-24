from flask import jsonify
from WebApp.blueprints.user import bp
from WebApp.blueprints.user.schemas import UserResponseSchema, UserRequestSchema, UserLoginSchema, RoleSchema ,AddressSchema, AddAddressSchema
from WebApp.blueprints.user.service import UserService
from apiflask import HTTPError
from apiflask.fields import String, Email, Nested, Integer, List
from WebApp.extensions import auth

@bp.route('/')
def index():
    return 'This is The User Blueprint'

@bp.post('/registrate')
@bp.doc(tags=["user"])
@bp.input(UserRequestSchema, location="json")
@bp.output(UserResponseSchema)
def user_registrate(json_data):
    success, response = UserService.user_registrate(json_data)
    if success:
        return response, 200

    raise HTTPError(message=response, status_code=400)

    

@bp.post('/login')
@bp.doc(tags=["user"])
@bp.input(UserLoginSchema, location="json")
@bp.output(UserResponseSchema)
def user_login(json_data):
    success, response = UserService.user_login(json_data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)




@bp.get('/roles')
@bp.doc(tags=["user"])
@bp.output(RoleSchema(many=True))
@bp.auth_required(auth)
def user_list_roles():
    success, response = UserService.user_list_roles()
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)


@bp.get('/roles/<int:uid>')
@bp.doc(tags=["user"])
@bp.output(RoleSchema(many=True))
@bp.auth_required(auth)
def user_list_user_roles(uid):
    success, response = UserService.list_user_roles(uid)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)


@bp.post('/address/update')
@bp.doc(tags=["user"])
@bp.input(AddAddressSchema, location="json")
def user_address_update(json_data):
    success, response = UserService.user_update_address(json_data)
    if success:
        return str(response), 200
    raise HTTPError(message=response, status_code=400)


@bp.delete('/delete/<int:uid>') # User törlés uid alapján
def user_delete(uid):
    success, response = UserService.user_delete(uid)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)


@bp.get('/list')  # Ki listázas az összes usert, amelyik usert nem töröltünk ki
@bp.output(UserResponseSchema(many = True))
def user_list_all():
    success, response = UserService.user_list_all()
    if success:
        return response, 200                                                            
    raise HTTPError(message=response, status_code=400)