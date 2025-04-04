from WebApp.blueprints.reservation import bp
from WebApp.blueprints.reservation.schemas import ReservationItemSchema, ReservationRequestSchema, ReservationResponseSchema
from WebApp.blueprints.reservation.service import ReservationService

from apiflask import HTTPError



@bp.route('/')
def index():
    return 'This is The Rooms Blueprint'


@bp.post('/add')  # foglalás hozzáadása
@bp.doc(tags=["reservation"])
@bp.input(ReservationRequestSchema,location="json")  
@bp.output(ReservationResponseSchema)  
def reservation_add_new(json_data):
    success, response = ReservationService.reservation_add(json_data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)

@bp.put('/update/<int:rid>')  # foglalás módosítása  
@bp.doc(tags=["reservation"])
@bp.input(ReservationRequestSchema, location="json")
@bp.output(ReservationResponseSchema)
def reservation_update(rid, json_data):
    success, response = ReservationService.reservation_update(rid, json_data)
    if success:
        return response, 200
    raise HTTPError(message=response, status_code=400)


