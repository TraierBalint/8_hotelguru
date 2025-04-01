from WebApp import db
from datetime import datetime

class Invoice(db.Model):
    __tablename__ = 'invoices'
    id = db.Column(db.Integer, primary_key=True)
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservations.id'), nullable=False)
    total_amount = db.Column(db.Float, nullable=False)
    issued_at = db.Column(db.DateTime, default=datetime.utcnow)
    paid = db.Column(db.Boolean, default=False)
    
    reservation = db.relationship("Reservation")