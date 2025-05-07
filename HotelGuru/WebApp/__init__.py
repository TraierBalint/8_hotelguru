from apiflask import APIFlask
from config import Config
from WebApp.extensions import db
from WebApp.models import *
from flask_cors import CORS

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
    CORS(app, origins='http://localhost:5173', methods=['GET', 'POST', 'PUT', 'DELETE'], supports_credentials=True)

    @app.get("/")
    def home():
        return {"message": "HotelGuru API is running"}
    
    from WebApp.blueprints import bp as bp_default
    app.register_blueprint(bp_default, url_prefix='/api')

    return app