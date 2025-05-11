from flask import Flask, render_template, redirect, url_for, request, flash, json
from flask_login import LoginManager, login_user, logout_user, current_user
from datetime import datetime
from Models.events_type import Event_type
from app import *
from Models.actor import Actor
from werkzeug.security import generate_password_hash, check_password_hash
from Models.users import Users
from Models.concert import Concert
from Models.performance import Performance
from Controlls.add_users import AddUsers
from Models.troupe import Troupe
from Models.genre import Genre
from Models.hall import Hall
from Models.show import Show
from Controlls.add_concert import AddConcert
from Controlls.add_performance import AddPerformance


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')


@app.route('/contacts', methods=["GET"])
def contacts():
    return render_template('contacts.html')


#авторизация администратора
@app.route('/admins_main', methods=["GET"])
def admins():
    return render_template('admins_main.html')


#авторизация обычного пользователя
@app.route('/users_main', methods=["GET"])
def users():
    return render_template('users_main.html')

#login
@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form.get('login')
        password = request.form.get('password')
        print(username, password)
        if not (username and password):
            flash('Заполните все поля')
            return redirect(url_for('login'))
        user = Users.query.filter_by(username=username).first()
        print(user)
        if not user or not check_password_hash(user.password, password):
            flash('Неверный логин или пароль')
            return redirect(url_for('login'))

        # Авторизация пользователя
        login_user(user)

        print('ayuuuuuuuu')
        if user.role == 'admin':
            return redirect(url_for('admins'))
        else:
            return redirect(url_for('users'))
    return render_template('login.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


#регистрация пользователя
@app.route('/registr', methods=["GET", "POST"])
def registr():
    if request.method == 'POST':
        username = request.form.get('login')
        password = request.form.get('password')
        print(username, password)
        if not (username and password):
            flash('Заполните все поля')
            return redirect(url_for('registr'))
        user = Users.query.filter_by(username=username).first()
        print(user)
        if user:
            flash('Придумайте другое имя, это занято. ')
            return redirect(url_for('registr'))
        else:
            new_user = Users(
                username=username,
                password=generate_password_hash(password),
                role='user'
            )
            addu = AddUsers()
            addu.add_users(new_user)
            user = Users.query.filter_by(username=username).first()
            print(user)
            login_user(user)
            print('ayuuuuuuuu')
            return redirect(url_for('users'))
    return render_template('registr.html')

#добавление мероприятий
@app.route('/add_mer', methods=["GET", "POST"])
def add_mer():
    all_actors = Actor.query.all()
    all_genres = Genre.query.all()
    db.create_all()

    if request.method == 'POST':
        name = request.form.get('name')
        format_type = request.form.get('format')
        genr = request.form.get('genre')
        print(genr)
        print(request.form)
        description = request.form.get('description')
        actor_names = request.form.getlist('actors')

        acc = request.form.get('accc')
        is_per = Performance.query.filter_by(name=name).first()
        is_con = Concert.query.filter_by(name=name).first()

        if format_type.lower() == 'performance' and not is_per:
            troupe = Troupe()
            for i in actor_names:
                actor1 = Actor.query.filter_by(name=i).first()
                troupe.actors.append(actor1)
            db.session.add(troupe)

            event = Event_type.query.filter_by(type=format_type).first()
            genre = Genre.query.filter_by(id=genr).first()

            perf = Performance(
                name=name,
                event_id=event.id,
                genre_id=genre.id,
                description=description,
                troupe_id=troupe.id
            )
            a = AddPerformance()
            a.add_performance(perf)
            print('All cool')
            db.session.commit()

        elif format_type.lower() == 'concert' and not is_con:
            event = Concert(name=name, description=description, actor=acc)
            db.session.add(event)
        else:
            return "Вы ввели неверные данные, попробуйте еще раз."

        db.session.commit()
        return render_template('add_mer.html', added=True)
    return render_template('add_mer.html', added=False, all_actors=all_actors, all_genres=all_genres)


#покупка билета
@app.route('/buy_ticket', methods=["GET", "POST"])
def buy_ticket():
    all_event_types = Event_type.query.all()
    all_halls = Hall.query.all()
    events = []
    shows = []

    if request.method == 'POST':
        selected_format = request.form.get('format')
        performance_id = request.form.get('performance_id')
        show_id = request.form.get('show_id')

        # Шаг 1: выбран формат, но не выбрано мероприятие
        if selected_format and not performance_id:
            if selected_format == 'Performance':
                events = Performance.query.all()
            elif selected_format == 'Concert':
                events = Concert.query.all()
            return render_template(
                'buy_ticket.html',
                all_event_types=all_event_types,
                selected_format=selected_format,
                all_halls=all_halls,
                events=events
            )

        # Шаг 2: выбран формат и мероприятие, показываем сеансы
        elif selected_format and performance_id and not show_id:
            if selected_format == 'Performance':
                selected_event = Performance.query.get(performance_id)
            elif selected_format == 'Concert':
                selected_event = Concert.query.get(performance_id)
            else:
                selected_event = None

            shows = Show.query.filter_by(event_id=performance_id).all()
            return render_template(
                'buy_ticket_shows.html',
                all_event_types=all_event_types,
                selected_format=selected_format,
                selected_event=selected_event,
                performance_id=performance_id,
                shows=shows,
                all_halls=all_halls
            )

        # Шаг 3: выбран сеанс (показ), можно идти на выбор места/покупку
        elif show_id:
            selected_show = Show.query.get(show_id)
            return render_template(
                'buy_ticket_final.html',
                show=selected_show
            )

    # Первый заход на страницу (GET)
    return render_template(
        'buy_ticket.html',
        all_event_types=all_event_types,
        selected_format=None,
        all_halls=all_halls
    )

#поиск актера
@app.route('/search_actor', methods=["GET", "POST"])
def search_actor():
    performances = []
    if request.method == 'POST':
        actor_name = request.form.get('actor_name')
        actor = Actor.query.filter_by(name=actor_name).first()
        # Все труппы, в которых он участвует
        troupes = actor.troupes
        performances = Performance.query.filter(Performance.troupe_id.in_([t.id for t in troupes])).all()

    return render_template('search_actor.html', performances=performances)

#добавление показа
@app.route('/add_events', methods=["GET", "POST"])
def add_events():
    all_event_types = Event_type.query.all()
    all_halls = Hall.query.all()
    events = []

    if request.method == 'POST':
        selected_format = request.form.get('format')
        performance_id = request.form.get('performance_id')

        if selected_format and not performance_id:
            if selected_format == 'Performance':
                events = Performance.query.all()
            elif selected_format == 'Concert':
                events = Concert.query.all()
            return render_template(
                'add_events.html',
                all_event_types=all_event_types,
                selected_format=selected_format,
                all_halls=all_halls,
                events=events)
        elif selected_format and performance_id:
            selected_format = request.form.get('format')
            performance_id = request.form.get('performance_id')
            start_datetime = request.form.get('start_datetime')
            end_datetime = request.form.get('end_datetime')
            hall_id = request.form.get('halla')

            print("Формат:", selected_format)
            print("ID события:", performance_id)
            print("Начало:", start_datetime)
            print("Конец:", end_datetime)
            print("Зал:", hall_id)

            is_per = Performance.query.filter_by(id=performance_id).first()
            is_con = Concert.query.filter_by(id=performance_id).first()
            is_time = Show.query.filter_by(date_start=start_datetime)
            formatt = Event_type.query.filter_by(type=selected_format).first()

            start = datetime.strptime(start_datetime, "%Y-%m-%dT%H:%M")
            end = datetime.strptime(end_datetime, "%Y-%m-%dT%H:%M")

            if is_time:
                if is_per:
                    show = Show(
                    type_id = formatt.id,
                    event_id=is_per.id,
                    date_start = start,
                    date_end = end,
                    hall_id = hall_id
                    )
                if is_con:
                    show = Show(
                        type_id=formatt.id,
                        event_id=is_con.id,
                        date_start=start,
                        date_end=end,
                        hall_id=hall_id
                    )
                db.session.add(show)
                print('All cool')
                db.session.commit()
            flash("Мероприятие успешно добавлено!")
            return redirect(url_for('add_events'))

    return render_template('add_events.html', all_event_types=all_event_types, all_halls=all_halls, selected_format=None)


#авторизация обычного пользователя
@app.route('/add_report', methods=["GET"])
def add_report():
    return render_template('add_report.html')

#метод скользящей средней
@app.route('/matem', methods=["GET"])
def matem():
    return render_template('matem.html')


if __name__ == '__main__':
    app.run()
