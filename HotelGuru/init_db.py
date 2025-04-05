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