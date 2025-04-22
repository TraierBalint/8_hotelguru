
    
from __future__ import annotations

import enum
from os import name

from WebApp.extensions import db
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String, Integer, Date
from sqlalchemy import ForeignKey
from sqlalchemy import Enum


class ReservationStatus(enum.Enum):
    ACTIVE = "active"
    CANCELLED = "cancelled"
    COMPLETED = "completed"

class Reservation(db.Model):  #nincs már benne az address id mert felesleges 
    __tablename__ = "reservations"
    id: Mapped[int] = mapped_column(primary_key=True)
    
    user_id: Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))
    user: Mapped[Optional["User"]] = relationship(back_populates="reservations")
    #items : Mapped[List["Rooms"]] = relationship(back_populates="Rooms", lazy=True)
    check_in: Mapped[Date] = mapped_column(Date())
    check_out: Mapped[Date] = mapped_column(Date())
    status: Mapped[ReservationStatus] = mapped_column(Enum(ReservationStatus), default=ReservationStatus.ACTIVE, nullable=False)
    #extraservices: Mapped[List["ExtraService"]] = relationship(back_populates="reservations")
    invoice: Mapped["Invoice"] = relationship(back_populates="reservations", uselist=False)
    reservation_rooms: Mapped[List["ReservationRoom"]] = relationship(
    back_populates="reservations",
    cascade="all, delete-orphan",
    passive_deletes=False)
    
        

