# this file is still in 'test' mode

# Routes for dashboard, analysis sessions
from flask import Blueprint, render_template, abort
from flask_login import login_required, current_user
from jinja2.exceptions import TemplateNotFound

main_bp = Blueprint(
    'main', 
    __name__
    # template_folder='templates',
    # url_prefix='/main'
)


@main_bp.route('/')
def homepage():
    try:
        return render_template('main/homepage.html')
    
    except TemplateNotFound:
        abort(500)


@main_bp.route('/dashboard')
@login_required # this works!!
def dashboard():
    return f"<h1>Welcome to your dashboard, {current_user.username}!</h1>"