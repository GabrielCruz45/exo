# this file is still in 'test' mode

# Routes for dashboard, analysis sessions
from flask import Blueprint, render_template, abort, request
from flask_login import login_required, current_user
from jinja2.exceptions import TemplateNotFound

from app.extensions import db

main_bp = Blueprint(
    'main', 
    __name__
)


@main_bp.route('/')
def homepage():
    try:
        return render_template('main/homepage.html')
    
    except TemplateNotFound:
        abort(500)


@main_bp.route('/dashboard', methods=['GET', 'POST'])
@login_required # this works!!
def dashboard():
    try:
        return render_template('main/dashboard.html', username=current_user.username)
    
    except TemplateNotFound:
        abort(500)
