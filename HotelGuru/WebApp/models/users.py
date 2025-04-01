from WebApp import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    phone = db.Column(db.String, nullable=True)
    address = db.Column(db.String, nullable=True)
    role = db.Column(db.String, nullable=False)

    reservations = db.relationship("Reservation", back_populates="guest")