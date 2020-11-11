
from wtforms import Form, BooleanField, StringField, PasswordField, SelectField,  validators

class RegistrationForm(Form):
    username = StringField('Username', [validators.Length(min=4, max=25)])
    email = StringField('Email Address', [validators.Length(min=6, max=35), validators.Email('Enter valid Email')])
    password = PasswordField('New Password', [
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    userStatus = SelectField('User Status', choices=("Business", "Individual"))