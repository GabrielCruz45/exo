# Routes for /login, /register, /logout
# This is where you'll write the logic to handle what happens when a user tries to register or log in.
from flask import Blueprint, render_template, abort, request, redirect, session
from jinja2.exceptions import TemplateNotFound


auth_bp = Blueprint(
    'auth', 
    __name__, 
    template_folder='templates/auth', 
    url_prefix='/auth'
)


# Create a /register route that accepts both GET and POST requests. If it's a POST
# request, validate the form data, create a new User object, set its password using your
# set
# _password method, add it to the database, and redirect the user to the login page
# with a success message.
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            # validate the form data,

            # create a new User object

            # set its password using your set_password method

            # add it to the database

            # redirect the user to the login page
            redirect('login.html') # check***********

        except TemplateNotFound:
            abort(500)
        
    else:
        try:
            return render_template('register.html')
        except:
            return





@auth_bp.route('/login')
def login():
    try:
        return
    except:
        return




@auth_bp.route('/logout')
def logout():
    try:
        return
    except:
        return







