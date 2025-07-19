Folder/File structure explanation:

    app/__init__.py (The Factory): This is the heart of the factory pattern. It will contain a function, create_app(), which initializes the Flask app, configures it, sets up extensions (from extensions.py), and registers all the blueprints (auth, main, admin). This makes your app instance easy to create for running or for testing.

    Blueprints (auth/, main/, admin/): Think of these as mini-applications. Each blueprint organizes the routes, templates, and logic for a specific part of your site. This prevents your main application file from becoming a massive, unreadable mess.

    app/analysis/core.py (The Brains): All your data science logic lives here. We intentionally keep it separate from the web-facing code (the routes). Your Flask routes will simply import functions from this file (e.g., calculate_esi_for_planets()) and pass data to them. This makes your analysis code reusable and easy to test independently.

    app/models.py (The Schema): Defines the structure of your database tables using SQLAlchemy's ORM. You'll have classes like User, CollaborationSession, etc., which map directly to tables in your database.

    run.py (The Ignition): A simple, clean script whose only job is to call create_app() from your factory and run the development server.