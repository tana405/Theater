
from app import *
from datetime import datetime
from Models.events_type import Event_type
from Models.hall import Hall
from Models.show import Show


with app.app_context():
    db.create_all()
    start = datetime.strptime("2025-01-01T18:00", "%Y-%m-%dT%H:%M")
    end = datetime.strptime("2025-01-01T19:00", "%Y-%m-%dT%H:%M")

    sss = Show(
        type_id = 1,
        event_id= 1,
        date_start = start,
        date_end = end,
        hall_id = 1
        )

    db.session.add(sss)
    print('All cool')
    db.session.commit()