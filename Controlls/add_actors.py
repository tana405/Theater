import sqlite3
from app import *
from Models.actors import Actors


class AddActors:
    def add_actors(self, new):
        existing_actors = Actors.query.filter_by(name=new.name).first()
        if not existing_actors:
            # Добавляем пользователя в базу данных
            with app.app_context():
                db.session.add(new)
                db.session.commit()
            print("Пользователь добавлен.")
        else:
            print("Пользователь уже существует.")

