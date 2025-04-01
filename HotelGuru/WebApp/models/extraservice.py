from WebApp import db

class ExtraService(db.Model):
    __tablename__ = 'extra_services'
    id = db.Column(db.Integer, primary_key=True)
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservations.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('services.id'), nullable=False)
    quantity = db.Column(db.Integer, default=1)

    reservation = db.relationship("Reservation")
    service = db.relationship("Service")