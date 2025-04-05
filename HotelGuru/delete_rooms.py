from WebApp.extensions import db
from WebApp.models.rooms import Rooms

# Mark all rooms as deleted
db.session.query(Rooms).update({'deleted': 1})
db.session.commit()
print("All rooms have been marked as deleted")
