
from werkzeug.security import check_password_hash, generate_password_hash
from app import *
from Models.performance import Performance
from Controlls.add_performance import AddPerformance


with app.app_context():
    db.create_all()

    troupe = Troupe()
    for i in actor_names:
        actor1 = Actor.query.filter_by(name=i).first()
        troupe.actors.append(actor1)
    db.session.add(troupe)

    event = Event_type.query.filter_by(name=format_type).first()
    genre = Genre.query.filter_by(name=genr).first()

    perf = Performance(
        name=name,
        event_id=event,
        genre_id=genre.id,
        description=description,
        troupe_id=troupe.id
    )
    a = AddPerformance()
    a.add_performance(perf)
    print('All cool')
    db.session.commit()



    new = Performance(
        name='Лебединое озеро',
        description='Драма о 8-летнем мальчике Саше Савельеве. Он живет у бабушки, потому что та не доверяет воспитание ребенка своей дочери, у которой новый муж и которая, по мнению бабушки, беспутная. Бабуля, настоящий тиран, и мать рвут ребенка на части.',
        hall='Камерный'
    )
    u1 = AddPerformance()
    u1.add_performance(new)