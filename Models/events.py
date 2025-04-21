from app import *
from flask_login import LoginManager, UserMixin, login_user

class Events(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    format = db.Column(db.String(30)) #performance или concert
    name = db.Column(db.String(100), unique=True)
    descryption = db.Column(db.String(200))
    actors = db.Column(db.String(200))

    def __repr__(self):
        return f'<Merop {self.username}>'
