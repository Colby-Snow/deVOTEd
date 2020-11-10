"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request
from deVOTEd import app
from .RegistrationForm import RegistrationForm
from .User import User

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/business')
def business():
    """Renders the contact page."""
    return render_template(
        'business.html',
        title='Business',
        year=datetime.now().year,
        message='Your business page.'
    )


@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data, form.userStatus.data)
        
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            if request.form['userStatus'] == "Business":
                return redirect(url_for("businesses"))
            if request.form['userStatus'] == "Individual":
                return redirect(url_for("individuals"))
    return render_template('login.html', error=error)

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/Individual')
def Individual():
    """Renders the about page."""
    return render_template(
        'Individual.html',
        title='Individual',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/businesses')
def businesses():
    """Renders the about page."""
    return render_template(
        'businesses.html',
        title='Businesses',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/marketplace')
def marketplace():
    """Renders the about page."""
    return render_template(
        'marketplace.html',
        title='marketplace',
        year=datetime.now().year,
        message='Your application description page.'
    )
