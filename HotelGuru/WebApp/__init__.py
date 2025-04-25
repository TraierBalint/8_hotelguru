from apiflask import APIFlask
from config import Config
from WebApp.extensions import db
from WebApp.models import *

def create_app(config_class=Config):
    app = APIFlask(
        __name__,
        json_errors=True,
        title="HotelGuru API",
        docs_path="/swagger"
    )

    app.config.from_object(config_class)

    db.init_app(app)

    from flask_migrate import Migrate
    migrate = Migrate(app, db, render_as_batch=True)

    @app.get("/")
    def home():
        return {"message": "HotelGuru API is running"}
    
    from WebApp.blueprints import bp as bp_default
    app.register_blueprint(bp_default, url_prefix='/api')

    return app
"""
    # Blueprintek regisztrálása
    from WebApp.blueprints.user import bp as user_bp
    app.register_blueprint(user_bp, url_prefix="/api/user")

    from WebApp.blueprints.rooms import bp as room_bp
    app.register_blueprint(room_bp, url_prefix="/api/room")

    from WebApp.blueprints.reservation import bp as res_bp
    app.register_blueprint(res_bp, url_prefix="/api/reservation")

    from WebApp.blueprints.extraservice import bp as extra_bp
    app.register_blueprint(extra_bp, url_prefix="/api/extraservice")

    from WebApp.blueprints.invoice import bp as invoice_bp
    app.register_blueprint(invoice_bp, url_prefix="/api/invoice")

    return app
""" """
from flask import Flask
from config import db_config
from urllib.parse import quote_plus
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

app = Flask(__name__)

# required for web forms
app.config["SECRET_KEY"] = "SecretKey123"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///Hotel.db"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from WebApp import routes, models, apiroutes
"""