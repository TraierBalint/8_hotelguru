from flask import jsonify
from WebApp.blueprints.user import bp
from WebApp.blueprints.user.schemas import UserResponseSchema, UserRequestSchema, UserLoginSchema, RoleSchema
from WebApp.blueprints.user.service import UserService
from apiflask import HTTPError
from apiflask.fields import String, Email, Nested, Integer, List
from WebApp.extensions import auth
from WebApp.blueprints import role_required
from flask_cors import cross_origin

@bp.route('/')
def index():
    return 'This is The User Blueprint'

@bp.post('/registrate')
@bp.doc(tags=["user"])
@bp.input(UserRequestSchema, location="json")
@bp.output(UserResponseSchema)
@cross_origin(origins="http://localhost:5173")
def user_registrate(json_data):
    success, response = UserService.user_registrate(json_data)
    if success:
        return response, 200

    raise HTTPError(message=response, status_code=400)

    

@bp.post('/login')
@bp.doc(tags=["user"])
@bp.input(UserLoginSchema, location="json")
@bp.output(UserResponseSchema)
@cross_origin(origins="http://localhost:5173")
def user_login(json_data):
    success, response = UserService.user_login(json_data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)




@bp.get('/roles')
@bp.doc(tags=["user"])
@bp.output(RoleSchema(many=True))
@bp.auth_required(auth)
@role_required(["Administrator"])#csak példának  de ha ezt a függvényt hívod meg azzal döntöd el melyik role fér a végponthoz
@cross_origin(origins="http://localhost:5173")
def user_list_roles():
    success, response = UserService.user_list_roles()
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)


@bp.get('/myroles')#itt ebben sokat changeltem (pl a nevét myroles-ra roles/<int:uid>)
@bp.doc(tags=["user"])
@bp.output(RoleSchema(many=True))
@bp.auth_required(auth)
@role_required(["User","Administrator","Receptionist"])
@cross_origin(origins="http://localhost:5173")
def user_list_user_roles():#már nem vár uid-t
    success, response = UserService.list_user_roles(auth.current_user.get("user_id"))#innen kivettem az uid-t és lecseréltem erre
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)


@bp.delete('/delete/<int:uid>') # User törlés uid alapján
@bp.auth_required(auth)
@role_required(["User"])#a kérdés hogy ezt csak a user törölheti-e vagy törölhesse az admin is?
@cross_origin(origins="http://localhost:5173")
def user_delete(uid):
    success, response = UserService.user_delete(uid)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)


@bp.get('/list')  # Ki listázas az összes usert, amelyik usert nem töröltünk ki
@bp.output(UserResponseSchema(many = True))
@bp.auth_required(auth)
@role_required(["Administrator"])
@cross_origin(origins="http://localhost:5173")
def user_list_all():
    success, response = UserService.user_list_all()
    if success:
        return response, 200                                                            
    raise HTTPError(message=response, status_code=400)