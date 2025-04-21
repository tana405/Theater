
from werkzeug.security import check_password_hash, generate_password_hash
from app import *
from Models.events import Events
from Controlls.add_events import AddEvents


with app.app_context():
    db.create_all()
    password = '5555'
    new = Events(
        username='anna',
        password=generate_password_hash(password),
        role='user'
    )
    u1 = AddEvents()
    u1.add_events(new)