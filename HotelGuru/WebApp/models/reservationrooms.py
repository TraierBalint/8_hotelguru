from __future__ import annotations

from typing import List, Optional
from WebApp.extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String, Integer
from sqlalchemy import ForeignKey

class ReservationRooms(db.Model):
    __tablename__ = "reservation_rooms"
    reservation_id: Mapped[int] = mapped_column(ForeignKey("reservations.id"), primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("Rooms.id"), primary_key=True)