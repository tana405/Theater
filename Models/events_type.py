from app import *

class Event_type(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(50))  # поле для определения типа события


    def __repr__(self):
        return f'<Event {self.name}>'
