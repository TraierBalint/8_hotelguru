from WebApp.extensions import db
from WebApp.blueprints.user.schemas import UserResponseSchema, RoleSchema, PayloadSchema
from WebApp.models.users import User
from WebApp.models.role import Role
from sqlalchemy import select

from datetime import datetime,timedelta
from authlib.jose import jwt, JsonWebKey
from flask import current_app

class UserService:
    
    @staticmethod
    def user_registrate(request):
        try:
            if db.session.execute(select(User).filter_by(email=request["email"])).scalar_one_or_none():
                return False, "E-mail already exist!"

            user = User(**request)
            user.set_password(user.password)
            user.roles.append(
                db.session.execute(select(Role).filter_by(name="User")).scalar_one_or_none()            
                )
            db.session.add(user)
            db.session.commit()
        except Exception as ex:
            return False, str(ex)#"Incorrect User data!"
        user_schema=UserResponseSchema().dump(user)
        user_schema["token"]=UserService.token_generate(user)
        return True, user_schema
    
    @staticmethod
    def user_login(request):
        try:
           user = db.session.execute(select(User).filter_by(email=request["email"])).scalar_one()
           if not user.check_password(request["password"]):
            return False, "Incorrect e-mail or password!"
           user_schema=UserResponseSchema().dump(user)
           user_schema["token"]=UserService.token_generate(user)
           return True, user_schema
        except Exception as ex:
            return False, str(ex)
        
    

    @staticmethod
    def token_generate(user:User):
        payload=PayloadSchema()
        payload.exp=int((datetime.now()+timedelta(days=1)).timestamp())
        payload.roles=RoleSchema().dump(user.roles, many=True)
        payload.user_id=user.id
        private_key = JsonWebKey.import_key(current_app.config["SECRET_KEY"], {'kty': 'RSA'})
        return jwt.encode({"alg": "RS256"},
                          PayloadSchema().dump(payload),
                          private_key).decode()
    
    @staticmethod
    def user_list_roles():
        roles = db.session.query(Role).all()
        return True, RoleSchema().dump(obj=roles, many=True)
    
    @staticmethod
    def list_user_roles(uid):
        user = db.session.get(User, uid)
        if user is None:
            return False, "User not found!"
        return True, RoleSchema().dump(obj=user.roles, many=True)
    
    #user törlés
    @staticmethod
    def user_delete(rid):
        try:
            user = db.session.get(User, rid)
            if user:
                db.session.delete(user)
                db.session.commit()
            
        except Exception as ex:
            return False, "user_update() error!"
        return True, "OK"
        
    #User listázás
    @staticmethod
    def user_list_all():
        users = db.session.execute(select(User)).scalars().all()
        return True, UserResponseSchema().dump(users, many = True) 