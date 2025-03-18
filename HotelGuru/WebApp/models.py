from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Float, Boolean
from sqlalchemy.orm import relationship, declarative_base
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=True)
    address = Column(String, nullable=True)
    role = Column(String, nullable=False)
    reservations = relationship("Reservation", back_populates="guest")

class Room(Base):
    __tablename__ = 'rooms'
    id = Column(Integer, primary_key=True)
    number = Column(String, unique=True, nullable=False)
    type = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    status = Column(String, default='available')
    reservations = relationship("Reservation", back_populates="room")

class Reservation(Base):
    __tablename__ = 'reservations'
    id = Column(Integer, primary_key=True)
    guest_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=False)
    check_in = Column(DateTime, nullable=False)
    check_out = Column(DateTime, nullable=False)
    confirmed = Column(Boolean, default=False)
    total_price = Column(Float, nullable=False)
    guest = relationship("User", back_populates="reservations")
    room = relationship("Room", back_populates="reservations")

class Service(Base):
    __tablename__ = 'services'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)

class ExtraService(Base):
    __tablename__ = 'extra_services'
    id = Column(Integer, primary_key=True)
    reservation_id = Column(Integer, ForeignKey('reservations.id'), nullable=False)
    service_id = Column(Integer, ForeignKey('services.id'), nullable=False)
    quantity = Column(Integer, default=1)
    reservation = relationship("Reservation")
    service = relationship("Service")

class Invoice(Base):
    __tablename__ = 'invoices'
    id = Column(Integer, primary_key=True)
    reservation_id = Column(Integer, ForeignKey('reservations.id'), nullable=False)
    total_amount = Column(Float, nullable=False)
    issued_at = Column(DateTime, default=datetime.utcnow)
    paid = Column(Boolean, default=False)
    reservation = relationship("Reservation")
