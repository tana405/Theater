from app import *
from Models.concert import Concerts
from Controlls.add_concert import AddConcerts
from Models.actor import Actors
from Controlls.add_actor import AddActors


with app.app_context():
    db.create_all()

    actor = Actors.query.filter_by(name='Алексеев Максим Петрович').first()
    if not actor:
        actor = Actors(
            name='Алексеев Максим Петрович',
            age='35',
            biography='Известный пианист'
        )
        db.session.add(actor)

    concert = Concerts.query.filter_by(name='Концерт имени Максимова М.М.').first()
    if not concert:
        concert = Concerts(
            name='Концерт имени Максимова М.М.',
            description='Талантливый скрипач представляет свой репертуар всей стране',
            hall='Камерный'
        )
        db.session.add(concert)

    # Привязка, если актёра ещё нет в концерте
    if actor not in concert.actors:
        concert.actors.append(actor)

    db.session.commit()
    print("Данные успешно добавлены!")

