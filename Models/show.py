from app import *


class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_id = db.Column(db.Integer, db.ForeignKey('event_type.id'))
    event_id = db.Column(db.Integer)
    date_start = db.Column(db.DateTime)
    date_end = db.Column(db.DateTime)
    hall_id = db.Column(db.Integer, db.ForeignKey('hall.id'))

    def __repr__(self):
        return f'<Shows {self.id}>'