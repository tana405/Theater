from app import *


class Place(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    zone_id = db.Column(db.Integer, db.ForeignKey('zone.id'))
    row = db.Column(db.String(20))
    plac = db.Column(db.String(20))

    def __repr__(self):
        return f'<Place {self.id}>'