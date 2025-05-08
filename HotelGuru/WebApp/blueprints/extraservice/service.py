from WebApp.extensions import db
from WebApp.models.extraservice import ExtraService
from WebApp.models.extraservice_order import ExtraServiceOrder
from WebApp.blueprints.extraservice.schemas import ExtraServiceResponseSchema,  ExtraServiceListResponseSchema
from sqlalchemy import select

class ExtraServiceService:

    @staticmethod
    def get_all():
        services = db.session.execute(select(ExtraService)).scalars().all()
        return True, ExtraServiceListResponseSchema().dump(services, many=True)

    @staticmethod
    def get_by_id(service_id):
        service = db.session.get(ExtraService, service_id)
        if not service:
            return False, "Extra service not found."
        return True, ExtraServiceListResponseSchema().dump(service)


    

    @staticmethod
    def create(data):
        try:
            new_order = ExtraServiceOrder(**data)  
            db.session.add(new_order)
            db.session.commit()
            return True, ExtraServiceResponseSchema().dump(new_order)
        except Exception as ex:
            db.session.rollback()
            return False, str(ex)

        
    @staticmethod
    def update(service_id, data):
        service = db.session.get(ExtraService, service_id)
        if not service:
            return False, "Extra service not found."
        try:
            for key, value in data.items():
                setattr(service, key, value)
            db.session.commit()
        except Exception as ex:
            return False, str(ex)
        return True, ExtraServiceResponseSchema().dump(service)

    @staticmethod
    def delete(service_id):
        service = db.session.get(ExtraService, service_id)
        if not service:
            return False, "Extra service not found."
        try:
            db.session.delete(service)
            db.session.commit()
        except Exception as ex:
            return False, str(ex)
        return True, "Deleted successfully."
