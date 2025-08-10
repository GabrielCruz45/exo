# Route for the user approval dashboard
from flask import Blueprint, render_template, abort, flash, redirect, url_for, abort
from flask_login import login_required
from jinja2 import TemplateNotFound
from sqlalchemy import select

from app.decorators import admin_required
from app.models import User
from app.extensions import db


admin_bp = Blueprint(
    'admin',
    __name__,
    # template_folder='templates',
    url_prefix='/admin'
)


@admin_bp.route('/dashboard')
@login_required
@admin_required
def admin_dashboard():
    try:
        # Inside this route, query the database for all users where is_approved is False.
        query = select(User.username, User.email).where(User.is_approved == False) # construct query to select only username and email
        results = db.session.execute(query).all() # list of row objects
        
        # Use list of unapproved users to create username, email dictionary
        unapproved_users = {username : email for username, email in results}

        return render_template('admin/admin_dashboard.html', unapproved_users=unapproved_users)
    
    except TemplateNotFound:
        return abort(500)


@admin_bp.route('/approve/<int:user_id>', methods=['POST'])
@login_required
@admin_required
def approve_user(user_id):

    # get user_id db info
    user = db.session.get(User, user_id)
    
    # error check
    if not user:
        return abort(404)
    
    # change approval status
    user.is_approved = True

    # commit change
    db.session.commit()


    flash('User successfully approved!', 'success')
    return redirect(url_for('admin.admin_dashboard'))
