"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import Flask, render_template, redirect, url_for, request, session
from deVOTEd import app
from .RegistrationForm import RegistrationForm
from .EventRegistrationForm import EventRegistrationForm
from .User import User
import deVOTEd.sqlConnection as connsql
import deVOTEd.inputtoHtml as intohtml
app.secret_key = "supersecretkeynoonewillevercheckeventhoughitsatthetopofthescreensotheycanseeiterror"

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

@app.route('/register', methods=['GET', 'POST'])
def register():
    """Renders the register page. Recieves register page and sends to sql db"""
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data, form.userStatus.data)
        cursor = connsql.initCursor()
        if(user.userStatus == "Business"):
            error = connsql.insertBusiness(cursor, user.username, user.password, 900, user.email)
        elif (user.userStatus == "Individual"):
            error = connsql.insertIndividuals(cursor, user.username, user.password, user.email)
        if(error == None):
            return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Renders the login page. Recieves register page info and sends to sql db"""
    error = None
    if request.method == 'POST':
        cursor = connsql.initCursor()
        if request.form['userStatus'] == "Business":
            userList = connsql.validateBusiness(cursor, request.form['username'], request.form['password'])
            if userList[0]:
                """Store Session variables here"""
                session['business_id'] = userList[1]
                session['userStatus'] = 'B'
                return redirect(url_for("businesses"))
            else:
                error = 'Invalid Credentials. Please try again.'
        elif request.form['userStatus'] == "Individual":
            userList = connsql.validateIndividual(cursor, request.form['username'], request.form['password'])
            if userList[0]:
                    """Store Session variables here"""
                    session['individual_id'] = userList[1]
                    session['userStatus'] = 'I'
                    return redirect(url_for("individuals"))
            else:
                error = 'Invalid Credentials. Please try again.'
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

@app.route('/individuals')
def individuals():
    """Renders the about page."""
    cursor = connsql.initCursor()
    connsql.updateCoinsIndividual(cursor)
    return render_template(
        'individuals.html',
        title='Individual',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/businesses')
def businesses():
    """Renders the about page."""
    cursor = connsql.initCursor()
    connsql.updateCoinsBusiness(cursor)
    return render_template(
        'businesses.html',
        title='Businesses',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/marketplace')
def marketplace():
    """Renders the marketplace page."""
    cursor = connsql.initCursor()
    cursor.execute("Select * from Items")
    return render_template(
        'marketplace.html',
        title='marketplace',
        year=datetime.now().year,
        items = cursor,
        columncount = 0
    )

@app.route('/item/<itemid>')
def item(itemid):
    """Renders the item page."""
    cursor = connsql.initCursor()
    cursor.execute("Select * from Items where item_id = ?", itemid)
    return render_template(
        'item.html',
        title='Market Item',
        year=datetime.now().year,
        item = cursor
    )

@app.route('/purchase/<itemid>')
def purchase(itemid):
    cursor = connsql.initCursor()
    
    
    if (session['userStatus'] == 'I'):
        connsql.purchaseIndiv(cursor, itemid, session['individual_id'])
        connsql.updateCoinsIndividual(cursor)
    else:
        connsql.purchaseBus(cursor, itemid, session['business_id'])
        connsql.updateCoinsBusiness(cursor)
    return redirect(url_for('marketplace'))


@app.route('/createEvent', methods=['GET', 'POST'])
def createEvent():
    """Renders the register page. Recieves register page and sends to sql db"""
    form = EventRegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        cursor = connsql.initCursor()
        connsql.insertEvent(cursor, form.eventName.data, form.eventDescription.data, form.eventCoins.data, form.eventDate.data, session['business_id'], form.eventLength.data)
        connsql.updateCoinsBusiness(cursor)
        return redirect(url_for('home'))
    return render_template('createevents.html', form=form)

@app.route('/events')
def events():
    cursor = connsql.initCursor()
    if (session['userStatus'] == 'I'):
        connsql.updateCoinsIndividual(cursor)
    else:
        connsql.updateCoinsBusiness(cursor)
    cursor.execute("Select * from Events")
    return render_template(
        'events.html',
        title='Events',
        year=datetime.now().year,
        events = cursor,
        intohtml = intohtml
    )

@app.route('/joinEvents/<eventid>')
def joinEvents(eventid):
    cursor = connsql.initCursor()
    connsql.joinEvent(cursor, eventid, session['individual_id'])
    if (session['userStatus'] == 'I'):
        connsql.updateCoinsIndividual(cursor)
    else:
        connsql.updateCoinsBusiness(cursor)
    return redirect(url_for('events'))

@app.route('/signout')
def signout():
    session.pop('individual_id', None)
    session.pop('business_id', None)
    session.pop('coins', None)
    return redirect(url_for('home'))


