# Route for the user approval dashboard
from flask import Blueprint, render_template, abort, flash, redirect, url_for, TemplateNotFound, abort
from flask_login import login_required

from app.decorators import admin_required
from app.models import User
from app.extensions import db


admin_bp = Blueprint(
    'admin',
    __name__,
    template_folder='templates',
    url_prefix='/admin'
)


@admin_bp.route('/dashboard')
@login_required
@admin_required
def admin_dashboard():
    try:
        # Inside this route, query the database for all users where is_approved is False. Pass this list of users to a new template.
        unapproved_users = db.session.execute(db.select(User).where(User.is_approved == False)).scalars().all()
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
