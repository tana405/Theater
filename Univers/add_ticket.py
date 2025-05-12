
from app import *
from Models.place import Place
from datetime import datetime
from Models.events_type import Event_type
from Models.zone import Zone
from Models.hall import Hall
from Models.show import Show
from Models.users import Users
from Models.ticket import Ticket


with app.app_context():
    db.create_all()

    sss = Ticket(
        place_id=1,
        price_id=1,
        user_id=1
    )

    db.session.add(sss)
    print('All cool')
    db.session.commit()