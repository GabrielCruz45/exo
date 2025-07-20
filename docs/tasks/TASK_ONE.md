Task 1: Application Skeleton and Initialization

Objective: To create the basic, runnable skeleton of the Flask application. By the end of this task, you will be able to start the server and see a simple "Hello, World!" page, proving that the core components are wired together correctly.

Estimated Time: 2-3 hours
Step 1: Define Project Dependencies

File to Modify: requirements.txt

Action:
Populate this file with the Python libraries we need for Phase 1. You will need to list one library per line. The key libraries are:

    Flask (the web framework itself)

    Flask-SQLAlchemy (for the database ORM)

    Flask-Migrate (for handling database migrations with Alembic)

    Flask-SocketIO (for real-time communication)

    python-dotenv (for managing environment variables, like your secret key)

    Pandas (for data manipulation)

Why: This file allows any developer (including you on a different computer) to install the exact same set of required packages using a single command (pip install -r requirements.txt), ensuring a consistent environment.

Documentation:

    Pip requirements.txt format

Step 2: Create the Configuration File

File to Modify: config.py

Action:

    Create a class named Config.

    Inside this class, define the configuration variables the application will use. For now, you need two:

        A SECRET_KEY. This is a long, random string that Flask uses to secure user sessions.

        A SQLALCHEMY_DATABASE_URI. This tells SQLAlchemy where to find the database. For now, we'll use a simple SQLite database.

    To keep your secret key out of your code (a critical security practice), you should load it from an "environment variable". The python-dotenv library helps with this. You'll create a new file named .env in the root exoplanet_analyzer/ directory to store the key.

Why: Separating configuration from code is crucial. It allows you to have different settings for development, testing, and production without changing the application logic.

Documentation:

    Flask Configuration Handling

    Flask-SQLAlchemy SQLALCHEMY_DATABASE_URI setting

Step 3: Set Up the Extension Initializer

File to Modify: app/extensions.py

Action:
Import the extension classes (e.g., SQLAlchemy, Migrate, SocketIO) and create an instance of each one. For example: db = SQLAlchemy(). Do this for all the Flask extensions you'll be using.

Why: By creating the instances here but not yet attaching them to a specific Flask app, we avoid a problem called "circular imports." These extension objects can then be safely imported and linked to our app inside the application factory.

Documentation:

    Flask-SQLAlchemy Application Setup (See the "Initialize the Extension" section for this pattern)

Step 4: Build the Application Factory

File to Modify: app/__init__.py

Action:
This is the most important step. You will create a function called create_app().

    Inside create_app(), create the Flask application instance: app = Flask(__name__).

    Load the configuration from your config.py file into the app.

    Import the extension objects (like db) from app/extensions.py and initialize them with your app instance using the init_app() method (e.g., db.init_app(app)).

    Import your blueprints (we'll create a simple one in the next step) and register them with the app.

    Return the app instance.

Why: The factory pattern allows us to create multiple instances of our application with different configurations, which is essential for testing and scaling. It makes the application's setup modular and predictable.

Documentation:

    Flask Application Factory Pattern

    Flask Blueprints (Specifically the "Registering Blueprints" section)

Step 5: Create the Main Blueprint and a Test Route

Files to Modify: app/main/__init__.py and app/main/routes.py

Action:

    In app/main/__init__.py, create the Blueprint instance: bp = Blueprint('main', __name__).

    In app/main/routes.py, import the blueprint (bp) and create a simple route for the homepage (/). This route should be a function that just returns a simple string like "Hello, Exoplanet Analyzer!".

    Remember to go back to your create_app function in app/__init__.py and register this blueprint.

Why: This tests that the factory, configuration, and blueprint registration are all working together. Seeing this message in your browser is the "green light" for this entire task.
Step 6: Create the Run Script

File to Modify: run.py

Action:

    Import the create_app function from your app package.

    Import the socketio instance from app.extensions.

    Call create_app() to create your application instance.

    Use a standard if __name__ == '__main__': block to run the application using socketio.run(app, debug=True).

Why: This file is the single entry point to start your application. Using socketio.run() instead of app.run() is important because it starts a server that understands both standard web requests and the WebSocket protocol needed for our chat feature.

Once you've completed these steps, open your terminal, navigate to the exoplanet_analyzer directory, install your requirements (pip install -r requirements.txt), and run the application (python run.py). If you see your "Hello" message in the browser, you have successfully completed your first task. Let me know how it goes!