#from flask import Blueprint
from apiflask import APIBlueprint

bp = APIBlueprint('main', __name__, tag="default")

@bp.route('/')
def index():
    return 'This is The Main Blueprint'

from WebApp.blueprints.user import bp as bp_user
bp.register_blueprint(bp_user, url_prefix='/user')

from WebApp.blueprints.rooms import bp as bp_rooms
bp.register_blueprint(bp_rooms, url_prefix='/rooms')


from WebApp.blueprints.reservation import bp as bp_reservation
bp.register_blueprint(bp_reservation, url_prefix='/reservation')

from WebApp.blueprints.extraservice import bp as bp_extraservice
bp.register_blueprint(bp_extraservice, url_prefix='/extraservice')
"""
from app.blueprints.chef import bp as bp_chef
bp.register_blueprint(bp_chef, url_prefix='/chef')

from app.blueprints.courier import bp as bp_courier
bp.register_blueprint(bp_courier, url_prefix='/courier')

from app.models import *"""