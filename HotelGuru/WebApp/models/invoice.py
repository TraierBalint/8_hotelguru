from __future__ import annotations

from WebApp.extensions import db
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String, Integer
from sqlalchemy import ForeignKey

class Invoice(db.Model):
    __tablename__ = 'invoices'
    id: Mapped[int] = mapped_column(primary_key=True)
    reservation_id: Mapped[int] = mapped_column(ForeignKey("reservations.id"), nullable=False)
    reservation: Mapped["Reservation"] = relationship(back_populates=("reservation"))
    total_amount:  Mapped[float] = mapped_column( nullable=False)
    issued_at: Mapped[str] = mapped_column( nullable=False)  # Date of issue
    paid: Mapped[bool] = mapped_column( default=False)  # Payment status
    