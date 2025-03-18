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
