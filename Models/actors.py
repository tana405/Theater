
from app import *
from flask_login import LoginManager, UserMixin, login_user

class Actors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    age = db.Column(db.String(20))
    biography = db.Column(db.String(100))
    perfomances = db.Column(db.String(200))

    def __repr__(self):
        return f'<Merop {self.name}>'

