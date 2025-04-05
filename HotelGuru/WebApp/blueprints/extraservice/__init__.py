from apiflask import APIBlueprint

bp = APIBlueprint('extraservice', __name__, tag="extraservice")

from WebApp.blueprints.extraservice import routes