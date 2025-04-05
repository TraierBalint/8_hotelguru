from WebApp import db

class Reservation(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer, primary_key=True)
    guest_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey('rooms.id'), nullable=False)
    check_in = db.Column(db.DateTime, nullable=False)
    check_out = db.Column(db.DateTime, nullable=False)
    confirmed = db.Column(db.Boolean, default=False)
    total_price = db.Column(db.Float, nullable=False)

    guest = db.relationship("User", back_populates="reservations")
    room = db.relationship("Rooms", back_populates="reservations")#Room volt, átírtam Rooms-ra