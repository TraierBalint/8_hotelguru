from apiflask import APIFlask
from config import Config
from WebApp.extensions import db
from WebApp.models import *

def create_app(config_class=Config):
    app = APIFlask(__name__, json_errors = True, 
               title="HotelGuru API",
               docs_path="/swagger")
    app.config.from_object(config_class)

    db.init_app(app)
    
    from flask_migrate import Migrate
    migrate = Migrate(app, db, render_as_batch=True)
    
    from WebApp.blueprints import bp as bp_default
    app.register_blueprint(bp_default, url_prefix='/api')

    return app

"""
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