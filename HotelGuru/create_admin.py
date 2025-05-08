from WebApp import create_app  # ← ez legyen az a függvény, ami létrehozza az appot
from WebApp.extensions import db
from WebApp.models import *
from WebApp.models.users import User
from WebApp.models.role import Role

app = create_app()  # létrehozzuk az appot

with app.app_context():
    # Létrehozás
    admin = User(
        name="Adminisztrátor",
        email="admin01@hotelguru.hu",
        phone="06301234567"
    )
    admin.set_password("asdasd123")  # jelszó

    # Administrator szerepkör keresése / létrehozása
    admin_role = db.session.execute(
        db.select(Role).filter_by(name="Administrator")
    ).scalar_one_or_none()

    if not admin_role:
        print("⚠️ Nincs Administrator szerepkör, létrehozom...")
        admin_role = Role(name="Administrator")
        db.session.add(admin_role)
        db.session.commit()

    admin.roles.append(admin_role)

    db.session.add(admin)
    db.session.commit()

    print("✅ Admin felhasználó (Administrator szerepkörrel) sikeresen létrehozva.")
