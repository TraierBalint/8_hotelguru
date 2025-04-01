from __future__ import annotations

from WebApp import db
from WebApp import create_app
from config import Config

app = create_app(config_class=Config)

app.app_context().push()