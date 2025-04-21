from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask import Migrate, Mail
import sqlite3

app = Flask(__name__)
app.secret_key = 'awesome'
app.template_folder = 'C:\\Users\\truno\\PycharmProjects\\Theater\\templates'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Add your database URI here
UPLOAD_FOLDER = 'C:\\Users\\truno\\PycharmProjects\\Theater\\'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)

log_manager = LoginManager()
log_manager.init_app(app)
#
# migrate = Migrate(app, db)
# mail = Mail(app)