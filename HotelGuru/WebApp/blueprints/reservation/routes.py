from WebApp.blueprints.reservation import bp
from WebApp.blueprints.reservation.schemas import  ReservationRequestSchema, ReservationResponseSchema,RoomsListSchema,ReservationUpdateSchema
from WebApp.blueprints.reservation.service import ReservationService

from apiflask import HTTPError



@bp.route('/')
def index():
    return 'This is The reservation Blueprint'


@bp.post('/add')
@bp.input(ReservationRequestSchema)
@bp.output(ReservationResponseSchema)
def add_reservation(json_data):
    success, result = ReservationService.reservation_add(json_data)
    if not success:
        raise HTTPError(400, result)
    return result

@bp.put('/update/<int:rid>')
@bp.input(ReservationUpdateSchema)
@bp.output(ReservationResponseSchema)
def update_reservation(rid, json_data):
    success, result = ReservationService.reservation_update(rid, json_data)
    if not success:
        raise HTTPError(400, result)
    return result

@bp.delete('/delete/<int:rid>')
def delete_reservation(rid):
    success, result = ReservationService.reservation_delete(rid)
    if not success:
        raise HTTPError(400, result)
    return {"message": result}

@bp.get('/list')
@bp.output(ReservationResponseSchema(many=True))
def list_reservations():
    success, result = ReservationService.reservation_list_all()
    return result

@bp.get('/user/<int:user_id>')
@bp.output(ReservationResponseSchema(many=True))
def list_reservations_by_user(user_id):
    success, result = ReservationService.reservation_list_by_user(user_id)
    return result

@bp.get('/rooms/<int:reservation_id>')
@bp.output(RoomsListSchema(many=True))  
def get_rooms_by_reservation(reservation_id):
    success, rooms_or_error = ReservationService.get_rooms_for_reservation(reservation_id)
    if not success:
        return {"message": rooms_or_error}, 404
    return rooms_or_error

@bp.get("/<int:rid>")
@bp.output(ReservationResponseSchema)
def get_reservation_by_id(rid):
    success, result = ReservationService.reservation_get_by_id(rid)
    if not success:
        raise HTTPError(404, result)
    return result

@bp.put('/cancel/<int:rid>')
@bp.output(ReservationResponseSchema)
def cancel_reservation(rid):
    success, result = ReservationService.reservation_cancel(rid)
    if not success:
        raise HTTPError(400, result)
    return result
