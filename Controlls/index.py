from flask import Flask, render_template, redirect, url_for, request, flash, json
from flask_login import LoginManager, login_user, logout_user, current_user
from app import *
from Models.actors import Actors
from werkzeug.security import generate_password_hash, check_password_hash
from Models.users import Users
from Models.events import Events
from Controlls.add_users import AddUsers


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
@app.route('/add_mer', methods=["GET"])
def add_mer():
    return render_template('add_mer.html')

#покупка билета
@app.route('/buy_ticket', methods=["GET"])
def buy_ticket():
    data = Users.query.all()  # Возвращает список объектов Data
    return render_template('buy_ticket.html', data=data)

#поиск актера
@app.route('/search_actor', methods=["GET"])
def search_actor():
    return render_template('search_actor.html')

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
