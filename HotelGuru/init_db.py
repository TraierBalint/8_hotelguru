from __future__ import annotations

from WebApp import db
from WebApp import create_app
from config import Config

app = create_app(config_class=Config)

app.app_context().push()

#Role
from WebApp.models.role import Role

db.session.add_all([ Role(name="Administrator"), 
                     Role(name="Receptionist"), 
                     Role(name ="User") ])
db.session.commit()
#User
from WebApp.models.users import User,  UserRole
from WebApp.models.address import Address
from WebApp.models.reservation import Reservation
from WebApp.models.invoice import Invoice
from WebApp.models.rooms import Rooms
from WebApp.models.extraservice import ExtraService
from WebApp.models.reservation_rooms import ReservationRoom
