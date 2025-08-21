# this file is still in 'test' mode

# Routes for dashboard, analysis sessions
import os
from flask import Blueprint, render_template, abort, current_app
from flask_login import login_required, current_user
from jinja2.exceptions import TemplateNotFound

from app.extensions import db
from app.analysis.core import load_exoplanet_data



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
        # os.path.join makes code more portable, prevents errors!
        file_path = os.path.join(current_app.root_path, '../', 'data', 'exo.csv')

        # load exoplanet data and convert to dictionary
        exoplanet_data = (load_exoplanet_data(file_path)).to_dict(orient='records')

        return render_template('main/dashboard.html', username=current_user.username, exoplanet_data=exoplanet_data)
    
    except TemplateNotFound:
        abort(500)
