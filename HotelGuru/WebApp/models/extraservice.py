
from __future__ import annotations

from WebApp.extensions import db
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String, Integer
from sqlalchemy import ForeignKey

class ExtraService(db.Model):
    __tablename__ = 'extraservices'
    id: Mapped[int] = mapped_column(primary_key=True)
    reservation_id: Mapped[int] = mapped_column(ForeignKey("reservations.id"), nullable=False)
    service_id: Mapped[int] = mapped_column(ForeignKey("services.id"), nullable=False)
    quantity: Mapped[int] = mapped_column(default=1)

    service: Mapped["Service"] = relationship(back_populates="extraservices")
    reservation: Mapped["Reservation"] = relationship(back_populates="extraservices")


    

