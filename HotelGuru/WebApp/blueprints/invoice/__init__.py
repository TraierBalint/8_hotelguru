from apiflask import APIBlueprint

bp = APIBlueprint('invoice', __name__, tag="invoice")

from WebApp.blueprints.invoice import routes