from flask import render_template, redirect, url_for, request, flash, jsonify
from flask_login import login_user, logout_user, current_user
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
from Models.place import Place
from Models.zone import Zone
from Models.ticket import Ticket
from Models.price import Price
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


@app.route('/buy_ticket', methods=["GET", "POST"])
def buy_ticket():
    if request.method == 'POST':
        performance_id = request.form.get('performance')
        show_id = request.form.get('show')
        zone_id = request.form.get('zone')
        row = int(request.form.get('row'))
        seat_number = int(request.form.get('seat_number'))

        print('33333333', zone_id)

        # Получаем данные о показе
        show = Show.query.filter_by(id=show_id).first()
        print(show)
        zone = Zone.query.filter_by(id=zone_id).first()
        print(zone)
        counts_place = zone.capacity
        print(counts_place)

        seats_in_row = 20  #в ряду 20 мест
        max_rows = counts_place // seats_in_row  #15 рядов
        if row <= max_rows and seat_number <= seats_in_row:
            # Проверка наличия свободного места для выбранной зоны

            seat = Place.query.filter_by(zone_id=zone_id, row=row, plac=seat_number).first()
            print(show.id, zone.id)
            price = Price.query.filter_by(show_id=show.id, zone_id=zone.id).first()
            print(price)
            print(show)
            if not seat:
                place = Place(
                    zone_id=zone.id,
                    row=row,
                    plac=seat_number
                )
                db.session.add(place)
                print('place: ', place)
                place = Place.query.filter_by(zone_id=zone.id, row=row, plac=seat_number).first()

                print('place: ', place)
                t = Ticket(
                    place_id=place.id,
                    price_id=price.id,
                    user_id=current_user.id
                )

                db.session.add(t)
                tt = Ticket.query.filter_by(place_id=place.id, price_id=price.id,
                    user_id=current_user.id).first()
                print(tt)
                print('All cool')


                db.session.commit()
                return redirect(url_for('success'))
            else:
                return "Место уже занято!", 400
        else:
            return "Неверные данные для ряда или места", 400

    plays = Concert.query.all()
    concerts = Performance.query.all()
    performances = plays + concerts
    return render_template('plaaace.html', performances=performances)


@app.route('/zones/<int:hall_id>')
def get_zones(hall_id):
    zones = Zone.query.filter_by(hall_id=hall_id).all()
    return jsonify([{
        'id': z.id,
        'name': z.name,
        'capacity': z.capacity}
        for z in zones])


@app.route('/shows/<performance_id>', methods=['GET'])
def get_shows(performance_id):
    shows = Show.query.filter_by(event_id=performance_id).all()
    return jsonify([{
        'id': s.id,
        'date_start': s.date_start.strftime('%Y-%m-%d %H:%M'),
        'hall_id': s.hall_id
    } for s in shows])



@app.route('/success')
def success():
    return "Билет успешно куплен!"

@app.route('/confirm_ticket', methods=['GET', 'POST'])
def confirm_ticket():
    global selected_show

    if not selected_show:
        flash("Ошибка: Показ не найден.")
        return redirect(url_for('buy_ticket'))

    # Получаем зоны и места
    zones = Zone.query.filter_by(hall_id=selected_show.hall_id).all()
    seats = Place.query.filter_by(hall_id=selected_show.hall_id).all()

    # Проверка на успешное получение данных
    print(f"Зоны: {zones}")
    print(f"Места: {seats}")
    print(f"Выбранный показ: {selected_show}")

    return render_template(
        'ticket_confirmation.html',
        seats=seats,
        zones=zones,
        selected_show=selected_show  # Передаем selected_show в шаблон
    )


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


@app.route('/add_report', methods=["GET"])
def add_report():
    shows = Show.query.all()
    report_data = None

    if request.method == 'POST':
        show_id = request.form.get('show_id')
        show = Show.query.get(show_id)

        if show:
            performance = Performance.query.get(show.performance_id)

            # Получение всех билетов для выбранного показа через Price → Ticket
            prices = Price.query.filter_by(show_id=show.id).all()
            price_ids = [p.id for p in prices]
            tickets_count = Ticket.query.filter(Ticket.price_id.in_(price_ids)).count()

            report_data = {
                'performance_name': performance.name,
                'start': show.date_start,
                'end': show.date_end,
                'tickets_sold': tickets_count
            }

    return render_template('add_report.html', shows=shows, report_data=report_data)


@app.route('/matem', methods=["GET"])
def matem():
    return render_template('matem.html')


if __name__ == '__main__':
    app.run()
