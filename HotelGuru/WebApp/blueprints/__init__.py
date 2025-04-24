#from flask import Blueprint
from apiflask import HTTPError
from apiflask import APIBlueprint
from functools import wraps

bp = APIBlueprint('main', __name__, tag="default")

@bp.route('/')
def index():
    return 'This is The Main Blueprint'

from WebApp.extensions import auth
from flask import current_app
from authlib.jose import jwt
from datetime import datetime

@auth.verify_token
def verify_token(token):
    try:
        if not token:
            return None
        public_key=current_app.config["SECRET_KEY"]
        data=jwt.decode(token.encode(),public_key)
        if data["exp"]< int(datetime.now().timestamp()):
            return None
        return data
    except:
        return None
    
def role_required(roles):#dekorátor és ezzel a függvényel tudsz végpontokat elérhetőve tenni az adott rolenak, ezt  routes.pyban hívod meg(lásd pl user routes.py roles vagy myroles)
    def wrapper(fn):
        @wraps(fn)
        def decorated_function(*args,**kwargs):
            user_roles=[item["name"] for item in auth.current_user.get("roles")]
            for role in roles:
                if role in user_roles:
                    return fn(*args,**kwargs)
            raise HTTPError(message="Access denied",status_code=403)
        return decorated_function
    return wrapper

    

from WebApp.blueprints.user import bp as bp_user
bp.register_blueprint(bp_user, url_prefix='/user')

from WebApp.blueprints.rooms import bp as bp_rooms
bp.register_blueprint(bp_rooms, url_prefix='/rooms')


from WebApp.blueprints.reservation import bp as bp_reservation
bp.register_blueprint(bp_reservation, url_prefix='/reservation')

from WebApp.blueprints.extraservice import bp as bp_extraservice
bp.register_blueprint(bp_extraservice, url_prefix='/extraservice')

from WebApp.blueprints.invoice import bp as bp_invoice
bp.register_blueprint(bp_invoice, url_prefix='/invoice')



