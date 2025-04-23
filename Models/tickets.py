from app import *
from halls import Halls
from shows import Shows


class Tickets(Halls, Shows, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    row = db.Column(db.String(20))
    place = db.Column(db.String(20))
    named = db.Column(db.String(40))

    def __repr__(self):
        return f'<Ticket {self.named}>'