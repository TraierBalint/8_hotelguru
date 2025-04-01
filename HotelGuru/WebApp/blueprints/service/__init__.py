#from flask import Blueprint
from apiflask import APIBlueprint

bp = APIBlueprint('service', __name__, tag="service")

from WebApp.blueprints.service import routes
