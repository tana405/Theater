
from werkzeug.security import check_password_hash, generate_password_hash
from app import *
from Models.actors import Actors
from Controlls.add_actors import AddActors


with app.app_context():
    db.create_all()
    new_actor = Actors(
    )
    u1 = AddActors()
    u1.add_actors(new_actor)