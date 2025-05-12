
from app import *
from datetime import datetime
from Models.events_type import Event_type
from Models.zone import Zone
from Models.hall import Hall
from Models.show import Show
from Models.place import Place


with app.app_context():
    db.create_all()


    sss = Place(
    zone_id=1,
    row=2,
    plac=2
    )

    db.session.add(sss)
    print('All cool')
    db.session.commit()