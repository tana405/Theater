from app import *


class Halls(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20)) #камерный или оперный
    tickets = db.Column(db.Integer)

    def __repr__(self):
        return f'<Halls {self.type}>'