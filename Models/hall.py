from app import *


class Hall(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(20)) #камерный или оперный

    def __repr__(self):
        return f'<Hall {self.type}>'