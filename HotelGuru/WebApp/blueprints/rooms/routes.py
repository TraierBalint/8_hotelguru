from WebApp.blueprints.rooms import bp
from WebApp.blueprints.rooms.schemas import RoomsListSchema , RoomsRequestSchema, RoomsResponseSchema
from WebApp.blueprints.rooms.service import RoomsService
from apiflask.fields import String, Integer
from WebApp.blueprints import role_required
from WebApp.extensions import auth
from apiflask import HTTPError

@bp.route('/')
def index():
    return 'This is The Rooms Blueprint'

@bp.get('/list')  # Ki listázas az összes szobát, amelyik szobát nem töröltünk ki
@bp.output(RoomsListSchema(many = True))
@bp.auth_required(auth)
@role_required(["User"])
def rooms_list_all():
    success, response = RoomsService.rooms_list_all()
    if success:
        return response, 200                                                            
    raise HTTPError(message=response, status_code=400)

@bp.delete('/delete/<int:rid>') # Szoba törlés rid alapján
def room_delete(rid):
    success, response = RoomsService.room_delete(rid)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.post('/add')  # Szoba hozzáadás

@bp.input(RoomsRequestSchema, location="json")
@bp.output(RoomsResponseSchema)
def room_add_new(json_data):
    success, response = RoomsService.room_add(json_data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.put('/update/<int:rid>') # Szoba frisítése id alapján
@bp.input(RoomsRequestSchema, location="json")
@bp.output(RoomsResponseSchema)
def room_update(rid, json_data):
    success, response = RoomsService.room_update(rid, json_data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)


@bp.get("/type/<string:type_name>")
@bp.output(RoomsListSchema(many=True))
def room_list_by_type(type_name):
    success, result = RoomsService.room_list_type(type_name)
    if not success:
        raise HTTPError(400, result)
    return result


@bp.get("/<int:rid>")  # Szoba listázása id alapján
@bp.output(RoomsResponseSchema)
def room_get_by_id(rid):
    success, result = RoomsService.room_get_by_id(rid)
    if not success:
        raise HTTPError(404, result)
    return result