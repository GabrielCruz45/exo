from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate
from flask_socketio import SocketIO
from flask_login import LoginManager

class Base(DeclarativeBase):
  pass

# gives you acces to db.Model class to define models and db.session for queries
db = SQLAlchemy(model_class=Base)

migrate = Migrate()

socketio = SocketIO()

login_manager = LoginManager()
login_manager.login_view = 'auth.login' # if user tries to access protected pages without permission