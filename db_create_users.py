from project import db
from project.models import User

db.session.add(User("Jake", "jake@gmail.com", "jake1231"))
db.session.add(User("Rose", "rose@hotmail.com", "eve"))

db.session.commit()