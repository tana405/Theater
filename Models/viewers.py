from app import *
from users import Users


class Viewers(Users, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))
    age = db.Column(db.String(20))
    account = db.Column(db.String(100)) #объект класса Users

    def __repr__(self):
        return f'<Viewers {self.name}>'
