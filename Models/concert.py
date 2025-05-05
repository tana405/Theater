from app import *


class Concert(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    description = db.Column(db.String(100))
    actor = db.Column(db.String(100))

    def __repr__(self):
        return f'<Concert {self.name}>'
