from app import *
from Models.performance import Performance


class AddPerformance:
    def add_performance(self, new):
        existing_events = Performance.query.filter_by(name=new.name).first()
        if not existing_events:
            db.session.add(new)
            print("Спектакль добавлен.")
        else:
            print("Спектакль уже существует.")

