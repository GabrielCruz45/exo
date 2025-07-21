from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, \
    SubmitField, DataRequired, Email, EqualTo, ValidationError


class LoginForrm(FlaskForm):
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


    def validate_username(username):
        
        if (): #
            return
    
    def validate_email():
        return
