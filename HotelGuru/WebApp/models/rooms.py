

from __future__ import annotations
import enum

from WebApp.extensions import db
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String, Integer
from sqlalchemy import Boolean, ForeignKey


"""class StatusEnum(enum.Enum):  
    SingleRoom  = 0,
    DoubleRoom  = 1,
    TwinRoom    = 2,
    Suites = 3,
    ConnectingRoom= 4, 
    DeluxRoom = 5
"""

class Rooms(db.Model):
    __tablename__ = "Rooms"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30)) 
    type : Mapped[str] = mapped_column()
    price : Mapped[int]
    status : Mapped[str] = mapped_column(default="available")
    deleted : Mapped[int] = mapped_column(default = 0) # ez lehetséges hogy nem kell
    reservation_rooms: Mapped[List["ReservationRoom"]] = relationship(back_populates="room")