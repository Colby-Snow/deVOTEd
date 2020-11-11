
from wtforms import Form, BooleanField, StringField, PasswordField, SelectField,  validators, DateTimeField, IntegerField

class EventRegistrationForm(Form):
    eventName = StringField('Event Name', [validators.Length(min=4, max=25)])
    eventDescription = StringField('Event Description', [validators.Length(min=4, max=300)])
    eventDate = DateTimeField('Event Date', format= '%m-%d-%Y')
    eventLength = IntegerField('Length in Hours')
    eventCoins = IntegerField('Total coins available')