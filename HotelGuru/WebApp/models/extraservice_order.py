from __future__ import annotations
from WebApp.extensions import db
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class ExtraServiceOrder(db.Model):
    __tablename__ = "extraservice_order"
    id: Mapped[int] = mapped_column(primary_key=True)
    
    reservation_id: Mapped[int] = mapped_column(ForeignKey("reservations.id", name="fk_extraservice_order_reservation_id", ondelete="CASCADE"))
    extraservice_id: Mapped[int] = mapped_column(ForeignKey("extraservices.id",name="fk_extraservice_order_extraservice_id", ondelete="CASCADE"))
    quantity: Mapped[int] = mapped_column(nullable=False)

    reservation: Mapped["Reservation"] = relationship(back_populates="extraservice_orders")
    extraservice: Mapped["ExtraService"] = relationship(back_populates="extraservice_orders")
    