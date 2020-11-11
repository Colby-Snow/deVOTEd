import pyodbc
from flask import session
import math

def initCursor():
    """Connects project to sql server and returns a cursor that can execute SQL server commands"""
    server = '(localdb)\MSSQLLocalDB' 
    database = 'DevotedDatabase' 
    username = 'sa' 
    password = 'serverpass' 
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    cursor = cnxn.cursor()
    return cursor

def insertIndividuals(cursor, name, password, email):
    cursor.execute("Select individual_name From Individuals Where individual_name = ?", name)
    if(cursor.rowcount != 0):
        isValid = True
    else:
        isValid = False

    if(not(isValid)):
        cursor.execute("Insert INTO Individuals(individual_name,individual_pass,individual_coins,individual_email) VALUES (?,?,?,?)", name, password, 0, email)
        cursor.commit()
        return None
    else:
        return "Error Username unavailable"

def insertBusiness(cursor, name, password, coins, email):
    cursor.execute("Select business_name From Businesses Where business_name = ?", name)
    if(cursor.rowcount != 0):
        isValid = True
    else:
        isValid = False

    if(not(isValid)):
        cursor.execute("Insert INTO Businesses(business_name,business_pass,business_coins, business_email) VALUES (?,?,?,?)", name, password, coins, email)
        cursor.commit()
        return None
    else:
        return "Error Username unavailable"

def insertMarketPlace(cursor, name, description, coins, imageurl, altimgurl = None, altimgurl2 = None):
    cursor.execute("Insert INTO items(item_name,item_description,item_coins,item_imgurl, item_altimgurl, item_altimgurl2) VALUES (?,?,?,?,?,?)", name, description, coins, imageurl, altimgurl, altimgurl2)
    cursor.commit()

def insertEvent(cursor, name, description, coins, date, businessId, length):
    cursor.execute("Update Businesses Set business_coins = business_coins - ? where business_id = ?", coins, businessId)
    calcpay = math.floor(coins/length)
    cursor.execute("Insert INTO Events(fk_business_id, event_name, event_description, event_date, event_coins, event_length, event_calcpay) VALUES (?,?,?,?,?,?,?)", businessId, name, description, date, coins, length, calcpay)
    cursor.commit()
    

def validateBusiness(cursor, username, password):
    cursor.execute("Select business_id, business_name, business_pass From Businesses Where business_name = ? and business_pass = ?", username, password)
    for row in cursor:
        businessId = row.business_id
    if(cursor.rowcount != 0):
        return [True, businessId]
    else:
        return [False]

def validateIndividual(cursor, username, password):
    cursor.execute("Select individual_id, individual_name, individual_pass From Individuals Where individual_name = ? and individual_pass = ?", username, password)
    for row in cursor:
        individualId = row.individual_id
    if(cursor.rowcount != 0):
        return [True, individualId]
    else:
        return [False]

def updateCoinsBusiness(cursor):
    if(session['business_id']):
        cursor.execute("Select business_coins from Businesses where business_id = ?", session["business_id"])
        for row in cursor:
            session['coins'] = row.business_coins
    
def updateCoinsIndividual(cursor):
    if(session['individual_id']):
        cursor.execute("Select individual_coins from Individuals where individual_id = ?", session["individual_id"])
        for row in cursor:
            session['coins'] = row.individual_coins

def joinEvent(cursor, eventId, individualId):
    cursor.execute("Select event_calcpay from Events Where event_id = ?", eventId)
    for row in cursor:
        coinsAdded = row.event_calcpay
    cursor.execute("Update Individuals Set individual_coins = individual_coins + ? where individual_id = ?", coinsAdded, individualId)
    cursor.execute("Insert Into IndividualSignups (fk_individual_id, fk_event_id) Values (?,?)", individualId,eventId)
    cursor.execute("Update Events Set event_coins = event_coins - ? where event_id = ?", coinsAdded, eventId)
    cursor.commit()

def purchaseIndiv(cursor, itemId, individualId):
    cursor.execute("Select item_coins from Items Where item_id = ?", itemId)
    for row in cursor:
        cost = row.item_coins
    cursor.execute("Update Individuals Set individual_coins = individual_coins - ? where individual_id = ?", cost, individualId)
    cursor.commit()

def purchaseBus(cursor, itemId, businessId):
    cursor.execute("Select item_coins from Items Where item_id = ?", itemId)
    for row in cursor:
        cost = row.item_coins
    cursor.execute("Update Businesses Set business_coins = business_coins - ? where business_id = ?", cost, businessId)
    cursor.commit()