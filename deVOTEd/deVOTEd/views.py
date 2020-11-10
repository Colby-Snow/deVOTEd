"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from deVOTEd import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
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
