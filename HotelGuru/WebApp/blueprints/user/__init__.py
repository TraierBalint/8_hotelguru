#from flask import Blueprint
from apiflask import APIBlueprint

bp = APIBlueprint('user', __name__, tag="user")

from WebApp.blueprints.user import routes
