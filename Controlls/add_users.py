import sqlite3
from app import *
from Models.users import Users


class AddUsers:
    def add_users(self, new_user):
        existing_user = Users.query.filter_by(username=new_user.username).first()
        if not existing_user:
            # Добавляем пользователя в базу данных
            with app.app_context():
                db.session.add(new_user)
                db.session.commit()
            print("Пользователь добавлен.")
        else:
            print("Пользователь уже существует.")


@log_manager.user_loader
def load_user(self):
    return Users.query.get(int(self))