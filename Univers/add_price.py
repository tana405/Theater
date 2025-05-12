
from app import *
from Models.events_type import Event_type
from Models.place import Place
from Models.zone import Zone
from Models.hall import Hall
from Models.show import Show
from Models.users import Users
from Models.ticket import Ticket
from Models.price import Price


with app.app_context():
    db.create_all()

    sss = Price(
        show_id=2,
        zone_id=1,
        price=1400
    )

    db.session.add(sss)
    print('All cool')
    db.session.commit()