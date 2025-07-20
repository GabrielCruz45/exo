from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_migrate import Migrate
from flask_socketio import SocketIO

class Base(DeclarativeBase):
  pass

# gives you acces to db.Model class to define models and db.session for queries
db = SQLAlchemy(model_class=Base)

migrate = Migrate()

socketio = SocketIO()