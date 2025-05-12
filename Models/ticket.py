from app import *
from Models.price import Price

class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    place_id = db.Column(db.Integer, db.ForeignKey('place.id'))
    price_id = db.Column(db.Integer, db.ForeignKey('price.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Ticket {self.id}>'