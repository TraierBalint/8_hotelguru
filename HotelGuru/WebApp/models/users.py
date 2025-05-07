
from WebApp.extensions import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import String, Integer
from sqlalchemy import ForeignKey, Column, Table
from typing import List, Optional
from werkzeug.security import generate_password_hash, check_password_hash

UserRole = Table(
    "userroles",
    Base.metadata,
    Column("user_id", ForeignKey("users.id", name="fk_userroles_user_id")),
    Column("role_id", ForeignKey("roles.id", name="fk_userroles_role_id"))
)


class User(db.Model):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    email: Mapped[Optional[str]]
    password: Mapped[str] = mapped_column(String(30))
    phone : Mapped[str] = mapped_column(String(30))
    roles: Mapped[List["Role"]] = relationship(secondary=UserRole, back_populates="users")
    reservations: Mapped[List["Reservation"]] = relationship(back_populates="user", lazy=True)
    
    
   
    

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!s}, email={self.email!r})"
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        
    def check_password(self, password):
        return check_password_hash(self.password, password)
  
       

