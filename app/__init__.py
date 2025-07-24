# Contains the Application Factory (create_app)
from flask import Flask
from .models import User

from .extensions import db, migrate, socketio, login_manager

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config') # reads the variables from your config.py file and loads them into the application itself

    # initialize extensions
    db.init_app(app)
    socketio.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # register blueprint
    with app.app_context():
        from .main.__init__ import homepage_bp
        app.register_blueprint(homepage_bp)

    return app