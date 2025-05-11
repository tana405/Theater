
from app import *
from datetime import datetime
from Models.hall import Hall
from Models.zone import Zone


with app.app_context():
    db.create_all()

    sss = Zone(
        name = "Партер",
        capacity = 300,
        hall_id = 2
        )
    db.session.add(sss)

    sss = Zone(
        name="Амфитеатр",
        capacity=175,
        hall_id=2
    )
    db.session.add(sss)

    sss = Zone(
        name="Балкон",
        capacity=150,
        hall_id=2
    )
    db.session.add(sss)

    sss = Zone(
        name="Партер",
        capacity=100,
        hall_id=1
    )
    db.session.add(sss)



    print('All cool')
    db.session.commit()


