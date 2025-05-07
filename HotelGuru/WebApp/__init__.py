from apiflask import APIFlask
from config import Config
from WebApp.extensions import db
from WebApp.models import *
from flask_cors import CORS
from flask import request, make_response


def create_app(config_class=Config):
    app = APIFlask(
        __name__,
        json_errors=True,
        title="HotelGuru API",
        docs_path="/swagger"
    )

    @app.before_request
    def handle_preflight():
        if request.method == 'OPTIONS':
            response = make_response()
            response.headers['Access-Control-Allow-Origin'] = 'http://localhost:5173'
            response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
            response.headers['Access-Control-Allow-Methods'] = 'GET,POST,PUT,DELETE,OPTIONS'
            return response

    app.config.from_object(config_class)

    db.init_app(app)

    from flask_migrate import Migrate
    migrate = Migrate(app, db, render_as_batch=True)

    CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

    @app.get("/")
    def home():
        return {"message": "HotelGuru API is running"}

    from WebApp.blueprints import bp as bp_default
    app.register_blueprint(bp_default, url_prefix='/api')

    return app
