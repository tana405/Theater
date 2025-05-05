import sqlite3
from app import *
from Models.actor import Actor


class AddActor:
    def add_actor(self, new):
        existing_actors = Actor.query.filter_by(name=new.name).first()
        if not existing_actors:
            db.session.add(new)
            print("Актер добавлен.")
        else:
            print("Актер уже существует.")

