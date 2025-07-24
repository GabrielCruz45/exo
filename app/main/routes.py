# this file is still in 'test' mode



# Routes for dashboard, analysis sessions
from flask import Blueprint, render_template, abort
from jinja2.exceptions import TemplateNotFound

homepage_bp = Blueprint('homepage', __name__, template_folder='templates') # change to url_prefix='/main'

@homepage_bp.route('/')
def homepage():
    try:
        return render_template('test/homepage.html')
    
    except TemplateNotFound:
        abort(500)
