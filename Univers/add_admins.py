
from werkzeug.security import check_password_hash, generate_password_hash
from app import *
from Models.users import Users
from Controlls.add_users import AddUsers


with app.app_context():
    db.create_all()
    password = '5555'
    new_user = Users(
        username='anna',
        password=generate_password_hash(password),
        role='user'
    )
    u1 = AddUsers()
    u1.add_users(new_user)
    password2 = '51416'
    new_admin = Users(
        username='tana',
        password=generate_password_hash(password2),
        role='admin'
    )
    #админ может создавать админов
    u2 = AddUsers()
    u2.add_users(new_admin)