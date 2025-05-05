from app import *
from Models.actor import actor_troupe


class Troupe(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    # Связь "многие ко многим" с актерами
    actors = db.relationship('Actor', secondary=actor_troupe, back_populates='troupes')


    def __repr__(self):
        return f'<Troupe {self.name}>'

