from WebApp.blueprints.rooms import bp
from WebApp.blueprints.rooms.schemas import RoomsListSchema , RoomsRequestSchema, RoomsResponseSchema
from WebApp.blueprints.rooms.service import RoomsService

from apiflask import HTTPError

@bp.route('/')
def index():
    return 'This is The Rooms Blueprint'

@bp.get('/list/')  # Ki listázas az összes szobát, amelyik szobát nem töröltünk ki
@bp.output(RoomsListSchema(many = True))
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