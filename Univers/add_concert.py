from app import *
from Models.concert import Concert
from Controlls.add_concert import AddConcert
from Models.actor import Actor
from Controlls.add_actor import AddActor


with app.app_context():
    db.create_all()

    actor = Actor.query.filter_by(name='Алексеев Максим Петрович').first()
    if not actor:
        actor = Actor(
            name='Алексеев Максим Петрович',
            age='35',
            biography='Известный пианист'
        )
        db.session.add(actor)

    concert = Concert.query.filter_by(name='Концерт имени Максимова М.М.').first()
    if not concert:
        concert = Concert(
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

