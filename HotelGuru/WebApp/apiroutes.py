from flask import Blueprint, request, jsonify
from WebApp.models import Users, Rooms, Reservation, Service, Invoice
from WebApp import db

apiroutes = Blueprint('apiroutes', __name__)

# User Management
@apiroutes.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = Users(name=data['name'], email=data['email'], phone=data.get('phone'), address=data.get('address'), role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@apiroutes.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = Users.query.get_or_404(user_id)
    return jsonify({'id': user.id, 'name': user.name, 'email': user.email, 'phone': user.phone, 'address': user.address, 'role': user.role})

@apiroutes.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.json
    user = Users.query.get_or_404(user_id)
    user.name = data['name']
    user.email = data['email']
    user.phone = data.get('phone')
    user.address = data.get('address')
    user.role = data['role']
    db.session.commit()
    return jsonify({'message': 'User updated successfully'})

@apiroutes.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = Users.query.get_or_404(user_id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'User deleted successfully'})

# Room Management
@apiroutes.route('/rooms', methods=['POST'])
def create_room():
    data = request.json
    new_room = Rooms(number=data['number'], type=data['type'], price=data['price'])
    db.session.add(new_room)
    db.session.commit()
    return jsonify({'message': 'Room created successfully'}), 201

@apiroutes.route('/rooms/<int:room_id>', methods=['GET'])
def get_room(room_id):
    room = Rooms.query.get_or_404(room_id)
    return jsonify({'id': room.id, 'number': room.number, 'type': room.type, 'price': room.price, 'status': room.status})

@apiroutes.route('/rooms/<int:room_id>', methods=['PUT'])
def update_room(room_id):
    data = request.json
    room = Rooms.query.get_or_404(room_id)
    room.type = data['type']
    room.price = data['price']
    room.status = data.get('status', room.status)
    db.session.commit()
    return jsonify({'message': 'Room updated successfully'})

@apiroutes.route('/rooms/<int:room_id>', methods=['DELETE'])
def delete_room(room_id):
    room = Rooms.query.get_or_404(room_id)
    db.session.delete(room)
    db.session.commit()
    return jsonify({'message': 'Room deleted successfully'})

# Reservation Management
@apiroutes.route('/reservations', methods=['POST'])
def create_reservation():
    data = request.json
    new_reservation = Reservation(guest_id=data['guest_id'], room_id=data['room_id'], check_in=data['check_in'], check_out=data['check_out'], total_price=data['total_price'])
    db.session.add(new_reservation)
    db.session.commit()
    return jsonify({'message': 'Reservation created successfully'}), 201

@apiroutes.route('/reservations/<int:reservation_id>', methods=['GET'])
def get_reservation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    return jsonify({'id': reservation.id, 'guest_id': reservation.guest_id, 'room_id': reservation.room_id, 'check_in': reservation.check_in, 'check_out': reservation.check_out, 'total_price': reservation.total_price})

@apiroutes.route('/reservations/<int:reservation_id>', methods=['PUT'])
def update_reservation(reservation_id):
    data = request.json
    reservation = Reservation.query.get_or_404(reservation_id)
    reservation.check_in = data['check_in']
    reservation.check_out = data['check_out']
    reservation.total_price = data['total_price']
    db.session.commit()
    return jsonify({'message': 'Reservation updated successfully'})

@apiroutes.route('/reservations/<int:reservation_id>', methods=['DELETE'])
def delete_reservation(reservation_id):
    reservation = Reservation.query.get_or_404(reservation_id)
    db.session.delete(reservation)
    db.session.commit()
    return jsonify({'message': 'Reservation deleted successfully'})

# Service Management
@apiroutes.route('/services', methods=['POST'])
def create_service():
    data = request.json
    new_service = Service(name=data['name'], price=data['price'])
    db.session.add(new_service)
    db.session.commit()
    return jsonify({'message': 'Service created successfully'}), 201

@apiroutes.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    service = Service.query.get_or_404(service_id)
    return jsonify({'id': service.id, 'name': service.name, 'price': service.price})

@apiroutes.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    data = request.json
    service = Service.query.get_or_404(service_id)
    service.name = data['name']
    service.price = data['price']
    db.session.commit()
    return jsonify({'message': 'Service updated successfully'})

@apiroutes.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    service = Service.query.get_or_404(service_id)
    db.session.delete(service)
    db.session.commit()
    return jsonify({'message': 'Service deleted successfully'})

# Invoice Management
@apiroutes.route('/invoices', methods=['POST'])
def create_invoice():
    data = request.json
    new_invoice = Invoice(reservation_id=data['reservation_id'], total_amount=data['total_amount'])
    db.session.add(new_invoice)
    db.session.commit()
    return jsonify({'message': 'Invoice created successfully'}), 201

@apiroutes.route('/invoices/<int:invoice_id>', methods=['GET'])
def get_invoice(invoice_id):
    invoice = Invoice.query.get_or_404(invoice_id)
    return jsonify({'id': invoice.id, 'reservation_id': invoice.reservation_id, 'total_amount': invoice.total_amount, 'issued_at': invoice.issued_at, 'paid': invoice.paid})

@apiroutes.route('/invoices/<int:invoice_id>', methods=['PUT'])
def update_invoice(invoice_id):
    data = request.json
    invoice = Invoice.query.get_or_404(invoice_id)
    invoice.total_amount = data['total_amount']
    invoice.paid = data.get('paid', invoice.paid)
    db.session.commit()
    return jsonify({'message': 'Invoice updated successfully'})

@apiroutes.route('/invoices/<int:invoice_id>', methods=['DELETE'])
def delete_invoice(invoice_id):
    invoice = Invoice.query.get_or_404(invoice_id)
    db.session.delete(invoice)
    db.session.commit()
    return jsonify({'message': 'Invoice deleted successfully'})