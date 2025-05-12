from app import *


class Zone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    capacity = db.Column(db.Integer)
    hall_id = db.Column(db.Integer, db.ForeignKey('hall.id'))

    def __repr__(self):
        return f'<Zone {self.id}>'