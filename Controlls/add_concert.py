import sqlite3
from app import *
from Models.concert import Concert


class AddConcert:
    def add_concert(self, new):
        existing_events = Concert.query.filter_by(name=new.name).first()
        if not existing_events:
            db.session.add(new)
            print("Концерт добавлен.")
        else:
            print("Концерт уже существует.")

