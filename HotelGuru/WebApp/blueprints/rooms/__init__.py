from apiflask import APIBlueprint

bp = APIBlueprint('rooms', __name__, tag="rooms")

from WebApp.blueprints.rooms import routes