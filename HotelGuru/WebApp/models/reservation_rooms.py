from __future__ import annotations
from WebApp.extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class ReservationRoom(db.Model):
    __tablename__ = "reservation_rooms"
    id: Mapped[int] = mapped_column(primary_key=True)
    
    reservation_id: Mapped[int] = mapped_column(ForeignKey("reservations.id"))
    room_id: Mapped[int] = mapped_column(ForeignKey("Rooms.id"))
    
    reservation: Mapped["Reservation"] = relationship(back_populates="reservation_rooms")
    room: Mapped["Rooms"] = relationship(back_populates="reservation_rooms")