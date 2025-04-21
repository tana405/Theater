import sqlite3
from app import *
from Models.events import Events


class AddEvents:
    def add_events(self, new):
        existing_events = Events.query.filter_by(name=new.name).first()
        if not existing_events:
            # Добавляем пользователя в базу данных
            with app.app_context():
                db.session.add(new)
                db.session.commit()
            print("Пользователь добавлен.")
        else:
            print("Пользователь уже существует.")

