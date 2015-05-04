from app import db
from project.users.views import bcrypt
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class BlogPost(db.Model):

    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    author_id = db.Column(db.Integer, ForeignKey('users.id'), nullable=False)

    def __init__(self, title, description, author_id):
        self.title = title
        self.description = description
        self.author_id = author_id

    def __repr__(self):
        return '<title {}'.format(self.title)


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.VARCHAR(10), nullable=False)
    email = db.Column(db.VARCHAR(100), nullable=False)
    passwd = db.Column(db.CHAR(60), nullable=False)
    posts = relationship("BlogPost", backref="author")

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.passwd = bcrypt.generate_password_hash(password)

    def __repr__(self):
        return '<name {}'.format(self.name)