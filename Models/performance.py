from app import *
from Models.events_type import Event_type


class Performance(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    event_id = db.Column(db.Integer, db.ForeignKey('event_type.id'))
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'))
    description = db.Column(db.String(100))
    troupe_id = db.Column(db.Integer, db.ForeignKey('troupe.id'))


    def __repr__(self):
        return f'<Performance {self.name}>'