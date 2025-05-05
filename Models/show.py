from app import *


class Show(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event_type.id'))
    date_start = db.Column(db.Datetime)
    date_end = db.Column(db.Datetime)
    hall_id = db.Column(db.Integer, db.ForeignKey('hall.id'))

    def __repr__(self):
        return f'<Shows {self.name}>'