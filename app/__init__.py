# Contains the Application Factory (create_app)
from flask import Flask, Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from extensions import db, migrate, socketio
from .. import config
# blueprint
from main import routes


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile(config)

    # initialize extensions
    db.init_app(app)
    socketio.init_app(app)
    migrate.init_app(app, db)

    # register blueprint
    app.register_blueprint(routes.homepage)

    return app