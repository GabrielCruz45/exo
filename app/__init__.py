# Contains the Application Factory (create_app)
from flask import Flask
from app.models import User, RoleEnum

from app.extensions import db, migrate, socketio, login_manager, assets

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config') # reads the variables from your config.py file and loads them into the application itself

    # initialize extensions
    db.init_app(app)
    socketio.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    assets.init_app(app)


    # provides critical link between the user ID stored in the browser's session_cookie and the actual user object in your database
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # defines a context processor; automatically makes "RoleEnum" available globally in Jinja2 templates
    @app.context_processor
    def inject_roles():
        return dict(RoleEnum=RoleEnum)

    # register the create admin command
    from . import commands
    app.cli.add_command(commands.create_admin)


    # register blueprint
    with app.app_context():
        from app.admin.routes import admin_bp
        from app.auth.routes import auth_bp
        from app.main.routes import main_bp
        
        app.register_blueprint(admin_bp)
        app.register_blueprint(auth_bp)
        app.register_blueprint(main_bp)

    return app