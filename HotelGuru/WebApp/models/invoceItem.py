from __future__ import annotations

from WebApp.extensions import db
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String, Integer, Date
from sqlalchemy import ForeignKey

class InvoiceItem(db.Model):
    __tablename__ = 'invoice_items'
    id: Mapped[int] = mapped_column(primary_key=True)
    invoice_id: Mapped[int] = mapped_column(ForeignKey("invoices.id"), nullable=False)
    item_type: Mapped[str] = mapped_column(nullable=False)  # 'room' vagy 'extra_service'
    item_id: Mapped[int] = mapped_column(nullable=False)  # Szoba vagy szolgáltatás azonosítója
    name: Mapped[str] = mapped_column(nullable=False)
    price: Mapped[float] = mapped_column(nullable=False)
    quantity: Mapped[int] = mapped_column(default=1)

    invoice: Mapped["Invoice"] = relationship(back_populates="items")
