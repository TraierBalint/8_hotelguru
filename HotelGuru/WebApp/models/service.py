
from __future__ import annotations

from WebApp.extensions import db
from typing import List, Optional
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String, Integer
from sqlalchemy import ForeignKey


class Service(db.Model):
    __tablename__ = 'services'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] =mapped_column(nullable=False)
    price: Mapped[float] = mapped_column()
    