from WebApp.blueprints.extraservice import bp
from apiflask import HTTPError
from WebApp.blueprints.extraservice.schemas import ExtraServiceListSchema
from WebApp.blueprints.extraservice.service import ExtraService


@bp.route('/')
def index():
    return 'This is The extraservice Blueprint'

@bp.get('/list/')  # Ki listázas az összes extraservicet
@bp.output(ExtraServiceListSchema(many = True))
def extraservice_list_all():
    success, response = ExtraService.extraservice_list_all()
    if success:
        return response, 200                                                            
    raise HTTPError(message=response, status_code=400)