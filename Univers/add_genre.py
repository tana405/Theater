
from app import *
from Models.genre import Genre


with app.app_context():
    db.create_all()
    new = Genre(
        name='Мюзикл'
    )
    db.session.add(new)

    new = Genre(
        name='Буффонада'
    )
    db.session.add(new)

    db.session.commit()