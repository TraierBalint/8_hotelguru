
    
from __future__ import annotations

import enum
from os import name

from WebApp.extensions import db
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String, Integer
from sqlalchemy import ForeignKey


class StatusEnum(enum.Enum):
    SingleRoom  = 0,
    DoubleRoom  = 1,
    Suites    = 2,
    TwinRoom = 3,
    StandardRoom= 4, 
    DeluxRoom = 5

class Reservation(db.Model):
    __tablename__ = "reservations"
    id: Mapped[int] = mapped_column(primary_key=True)
    
    user_id : Mapped[Optional[int]] = mapped_column(ForeignKey("users.id"))
    user : Mapped[Optional["User"]] = relationship(back_populates="reservations")
    
    address_id : Mapped[int] = mapped_column(ForeignKey("addresses.id"))
    address : Mapped["Address"] = relationship(back_populates="reservations")
    #items : Mapped[List["Rooms"]] = relationship(back_populates="Rooms", lazy=True) ebbe nem cagyok biztos 
    

