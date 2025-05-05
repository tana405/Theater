from app import *


class Zone(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Integer, db.ForeignKey('events_type.id'))
    capacity = db.Column(db.Integer)
    hall_id = db.Column(db.Integer, db.ForeignKey('hall.id'))

    def __repr__(self):
        return f'<Shows {self.name}>'