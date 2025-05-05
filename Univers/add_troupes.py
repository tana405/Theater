
from Models.troupe import Troupe
from datetime import datetime
from app import *
from Models.actor import Actor
from Controlls.add_actor import AddActor


with app.app_context():
    db.create_all()
    actor1 = Actor.query.filter_by(name='Захаров Харитон Радеонович').first()
    actor2 = Actor.query.filter_by(name='Нечаева Екатерина Андреевна').first()

    troupe1 = Troupe()

    troupe1.actors.append(actor1)
    troupe1.actors.append(actor2)
    db.session.add(troupe1)
    print('All cool')
    db.session.commit()