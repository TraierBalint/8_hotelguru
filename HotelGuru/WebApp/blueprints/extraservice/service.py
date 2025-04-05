from WebApp.blueprints.extraservice.schemas import ExtraServiceListSchema, ExtraServiceResponseSchema
from WebApp.extensions import db
from WebApp.models.extraservice import ExtraService
from sqlalchemy import select

class ExtraService:
    @staticmethod   
    def extraservice_list_all():
        extraservice = db.session.execute( select(ExtraService).filter(ExtraService.deleted.is_(0))).scalars()
        return True, ExtraServiceResponseSchema().dump(extraservice, many = True) 