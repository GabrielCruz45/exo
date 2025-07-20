# Routes for dashboard, analysis sessions
from flask import render_template, abort
from __init__ import homepage_bp

@homepage_bp.route('/')
def homepage():
    try:
        return render_template('index.html')
    except:
        abort(404, description="Practicing try ..except code block")
