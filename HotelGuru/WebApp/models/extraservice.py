
from __future__ import annotations

from WebApp.extensions import db
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String, Integer , Float
from sqlalchemy import ForeignKey

class ExtraService(db.Model):
    __tablename__ = 'extraservices'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    price: Mapped[float] = mapped_column(Float, nullable=False)
    #reservation_id: Mapped[int] = mapped_column(ForeignKey("reservations.id"), nullable=False)
    #reservations: Mapped[Optional['Reservation']] = relationship(back_populates='extraservices')
    
    


    

