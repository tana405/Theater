from app import *
from events import Events


class Concerts(Events, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    actors = db.Column(db.String(20))
    description = db.Column(db.String(100))
    hall = db.Column(db.String(200))
    tickets = db.Column(db.Integer)

    def __repr__(self):
        return f'<Concert {self.name}>'
