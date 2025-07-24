from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, \
    SubmitField, DataRequired, Email, EqualTo, ValidationError

from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()]) # check to change for password_hash
    remember_me = BooleanField('Remember me')
    submit_button = SubmitField('Submit')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    repeat_password = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password', message='Password fields must match')]
    )
    submit_button = SubmitField('Submit')


    # query the database to check if username and email already in use
    def validate_username(self, username):
        userQuery = User.query.filter_by(username=username.data).first()
        if userQuery:
            raise ValidationError("That username is already taken, choose another one.")
                
    def validate_email(self, email):
        emailQuery = User.query.filter_by(email=email.data).first()
        if emailQuery:
            raise ValidationError("That email is already taken, use another one.")
