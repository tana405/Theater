from app import *
from Models.hall import Hall


with app.app_context():
    db.create_all()
    new = Hall(
        type='Камерный'
    )
    db.session.add(new)

    new = Hall(
        type='Оперный'
    )
    db.session.add(new)

    db.session.commit()