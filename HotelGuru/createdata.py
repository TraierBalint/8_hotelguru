from WebApp.extensions import db
from WebApp import create_app
from WebApp.models import *
from WebApp.models.rooms import Rooms, RoomStatus, RoomType
from flask import Flask

app = create_app()
app.app_context().push()


# Feltöltendő szobák
sample_rooms = [
    {"name": "101 - Egyágyas", "type": RoomType.SINGLE, "price": 12000, "status": RoomStatus.AVAILABLE},
    {"name": "102 - Kétágyas", "type": RoomType.DOUBLE, "price": 18000, "status": RoomStatus.AVAILABLE},
    {"name": "201 - Lakosztály", "type": RoomType.SUITE, "price": 35000, "status": RoomStatus.RESERVED},
    {"name": "202 - Kétágyas", "type": RoomType.DOUBLE, "price": 19000, "status": RoomStatus.MAINTENANCE},
    {"name": "301 - Egyágyas", "type": RoomType.SINGLE, "price": 11500, "status": RoomStatus.AVAILABLE},
]

with app.app_context():
    for room_data in sample_rooms:
        room = Rooms(**room_data)
        db.session.add(room)

    db.session.commit()
    print("Szobák sikeresen feltöltve!")
