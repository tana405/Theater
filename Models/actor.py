from app import *

# Промежуточная таблица для связи "многие ко многим"
actor_troupe = db.Table('actor_troupe',
    db.Column('actor_id', db.Integer, db.ForeignKey('actor.id'), primary_key=True),
    db.Column('troupe_id', db.Integer, db.ForeignKey('troupe.id'), primary_key=True)
)

class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), unique=True)
    birthday = db.Column(db.Date)
    biography = db.Column(db.String(100))

    troupes = db.relationship('Troupe', secondary=actor_troupe, back_populates='actors')

    def __repr__(self):
        return f'<Actor {self.name}>'
