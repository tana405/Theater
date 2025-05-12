from app import *
from Models.show import Show


class Price(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    show_id = db.Column(db.Integer, db.ForeignKey('show.id'))
    zone_id = db.Column(db.Integer, db.ForeignKey('zone.id'))
    price = db.Column(db.Integer)

    def __repr__(self):
        return f'<Price {self.id}>'