from apiflask import APIBlueprint

bp = APIBlueprint('reservation', __name__, tag="reservation")

from WebApp.blueprints.reservation import routes