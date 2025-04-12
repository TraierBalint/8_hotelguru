from WebApp.blueprints.reservation import bp
from WebApp.blueprints.reservation.schemas import  ReservationRequestSchema, ReservationResponseSchema
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
@bp.input(ReservationRequestSchema)
@bp.output(ReservationResponseSchema)
def update_reservation(rid, data):
    success, result = ReservationService.reservation_update(rid, data)
    if not success:
        raise HTTPError(400, result)
    return result

@bp.delete('/delete/<int:rid>')
def delete_reservation(rid):
    success, result = ReservationService.reservation_delete(rid)
    if not success:
        raise HTTPError(400, result)
    return {"message": result}

@bp.get('/')
@bp.output(ReservationResponseSchema(many=True))
def list_reservations():
    success, result = ReservationService.reservation_list_all()
    return result

@bp.get('/user/<int:user_id>')
@bp.output(ReservationResponseSchema(many=True))
def list_reservations_by_user(user_id):
    success, result = ReservationService.reservation_list_by_user(user_id)
    return result
