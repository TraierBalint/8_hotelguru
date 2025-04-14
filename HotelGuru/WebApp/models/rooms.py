

from __future__ import annotations
import enum

from WebApp.extensions import db
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String, Integer
from sqlalchemy import Boolean, ForeignKey
from sqlalchemy import Enum
import enum

class RoomStatus(enum.Enum): #müködik az enum
    AVAILABLE = "available"
    RESERVED = "reserved"
    MAINTENANCE = "maintenance"

class RoomType(enum.Enum):
    SINGLE = "single"
    DOUBLE = "double"
    SUITE = "suite"

class Rooms(db.Model):
    __tablename__ = "Rooms"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30)) 
    type : Mapped[RoomType] = mapped_column(Enum(RoomType), nullable=False) # enumot nem tudom hogy kell
    price : Mapped[int]
    status: Mapped[RoomStatus] = mapped_column(Enum(RoomStatus), default=RoomStatus.AVAILABLE, nullable=False)  #így helyes
    #deleted : Mapped[int] = mapped_column(default = 0) # ez lehetséges hogy nem kell
    reservation_rooms: Mapped[List["ReservationRoom"]] = relationship(back_populates="room")