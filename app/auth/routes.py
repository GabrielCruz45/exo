# Routes for /login, /register, /logout
# This is where you'll write the logic to handle what happens when a user tries to register or log in.
from flask import Blueprint, render_template, abort, request, redirect, session, url_for, flash
from flask_login import login_user, logout_user
from jinja2.exceptions import TemplateNotFound

from app.auth.forms import RegistrationForm, LoginForm
from app.models import User, RoleEnum
from app.extensions import db



auth_bp = Blueprint(
    'auth', 
    __name__, 
    # template_folder='templates', 
    url_prefix='/auth'
)



@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    # get user input from form
    form = RegistrationForm(request.form)

    # validate the form data,
    if form.validate_on_submit(): # 'samey' as -> request.method == 'POST' and form.validate()

        # create a new User object
        new_user = User(
            username = form.username.data,
            email = form.email.data,
            role = RoleEnum.user
        )

        # set its password using your set_password method
        new_user.set_password(form.password.data)

        # add it to the database
        db.session.add(new_user)
        db.session.commit()
        
        # login user, send message
        login_user(new_user)
        flash("Registration successful! Redirecting to dashboard.", 'success')

        # redirect new, logged in user to the login page
        return redirect(url_for('main.dashboard'))

    # else if 'GET' -> if form.validate_on_submit(): handles this too
    try:
        return render_template('auth/register.html', form=form)
    
    except TemplateNotFound:
        return abort(500)



@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    # get user input on login form
    form = LoginForm(request.form)

    if form.validate_on_submit():
        # find the user by their username
        user = User.query.filter_by(username=form.username.data).first()
        
        # first check if -> user exists and password matches
        if user and user.check_password(form.password.data):

            # check if user is approved by admin
            if user.is_approved:
                login_user(user)
                print(f"user role: {user.role}")
                # if user.RoleEnum == RoleEnum.admin:
                    # return redirect
                return redirect(url_for('main.dashboard'))
            
            # error because approval
            else:
                flash('Still pending approval', 'warning')
                return redirect(url_for('auth.login'))
        
        # error because username does not exist
        else:
            flash('Wrong username and/or password.', 'danger')
            return redirect(url_for('auth.login'))

    # else if 'GET'
    try:
        return render_template('auth/login.html', form=form)
    
    except TemplateNotFound:
        return abort(500)




@auth_bp.route('/logout')
def logout():
    logout_user()
    session.clear() # mega-ultra-super-duper defense
    return redirect(url_for('main.homepage'))
