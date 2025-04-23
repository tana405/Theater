from app import *


class Shows(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    date = db.Column(db.Datetime)
    description = db.Column(db.String(100))
    hall = db.Column(db.String(200))
    tickets = db.Column(db.Integer)

    def __repr__(self):
        return f'<Shows {self.name}>'