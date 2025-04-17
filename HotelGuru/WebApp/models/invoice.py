from __future__ import annotations

from WebApp.extensions import db
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String, Integer, Date
from sqlalchemy import ForeignKey

class Invoice(db.Model):
    __tablename__ = 'invoices'
    id: Mapped[int] = mapped_column(primary_key=True)
    reservation_id: Mapped[int] = mapped_column(ForeignKey("reservations.id"), nullable=False)
    
    total_amount:  Mapped[float] = mapped_column( nullable=False)
    issued_at: Mapped[Date] = mapped_column(Date(), nullable=False)  # Date of issue
    paid: Mapped[bool] = mapped_column( default=False)  # Payment status

    reservations: Mapped["Reservation"] = relationship(back_populates="invoice")
    items: Mapped[List["InvoiceItem"]] = relationship(back_populates="invoice", cascade="all, delete-orphan")