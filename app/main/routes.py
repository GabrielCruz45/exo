# Routes for dashboard, analysis sessions
from flask import render_template, abort
from .__init__ import homepage_bp

@homepage_bp.route('/')
def homepage():
    # try:
    print("klk")
    return 'Hello, this is an Exoplanet Analyzer!'
    # except:
    #     abort(404, description="Practicing try ..except code block, and you've got an error! >.<")
