from flask import Flask, render_template, redirect, url_for, request, flash, json
from flask_login import LoginManager, login_user, logout_user, current_user

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
@app.route('/buy_ticket', methods=["GET"])
def buy_ticket():
    data = Users.query.all()  # Возвращает список объектов Data
    return render_template('buy_ticket.html', data=data)

#поиск актера
@app.route('/search_actor', methods=["GET"])
def search_actor():
    query = request.args.get('query', '').strip()
    results = []
    if query:
        results += Performance.query.filter(Performance.actors.ilike(f'%{query}%')).all()
        results += Concert.query.filter(Concert.actors.ilike(f'%{query}%')).all()

    return render_template('search_actor.html', results=results, query=query)

#добавление показа
@app.route('/add_events', methods=["GET"])
def add_events():
    return render_template('add_events.html')

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
