from WebApp import db

class Rooms(db.Model):
    __tablename__ = 'rooms'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.String, unique=True, nullable=False)
    type = db.Column(db.String, nullable=False)
    price = db.Column(db.Float, nullable=False)
    status = db.Column(db.String, default='available')

    reservations = db.relationship("Reservation", back_populates="room")