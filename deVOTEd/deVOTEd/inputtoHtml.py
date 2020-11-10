def main():
    itemMain()
    print("<br>\n")
    eventsMain()
    print("<br>\n")
    businessMain()
    print("<br>\n")
    individualMain()
    print("\n")

def itemMain():
    getItem = itemInit()
    itemID, itemName, itemDescription, itemImgurl, itemCoins = splitItem(getItem)
    itemsTable(itemID, itemName, itemDescription, itemImgurl, itemCoins)

def itemInit():
    item = ("420123, Apple, Literaly an apple., https://i5.walmartimages.ca/images/Large/094/514/6000200094514.jpg, 1000")
    getItem = item.split(",")
    return getItem

def splitItem(getItem):
    itemID= getItem[0]
    itemName = getItem[1]
    itemDescription= getItem[2]
    itemImgurl= getItem[3]
    itemCoins= getItem[4]
    return itemID, itemName, itemDescription, itemImgurl, itemCoins

def itemsTable(itemID, itemName, itemDescription, itemImgurl, itemCoins):
    print("<table>")
    print("<tr>")
    print("<th>",'ID',"</th>")
    print("<th>",'Name',"</th>")
    print("<th>",'Item Description',"</th>")
    print("<th>",'Image',"</th>")
    print("<th>",'Coins',"</th>")
    print("</tr>")
    print("<tr>")
    print("<td>",str(itemID),"</td>")
    print("<td>",str(itemName),"</td>")
    print("<td>",str(itemDescription),"</td>")
    print("<td>""<img src ="'"',str(itemImgurl), '"'"alt="'"'"Apple"'"', "width="'"'"50"'"',  "height="'"'"50"'"', ">""</td>")
    print("<td>",str(itemCoins),"</td>")
    print ("</tr>")
    print("</table>")

def eventsMain():
    getEvent = eventInit()
    eventID, businessID, eventDate, eventCoins = splitEvent(getEvent)
    eventsTable(eventID, businessID, eventDate, eventCoins)

def eventInit():
    event = ("420123, 71327, 11/11/2020, 90")
    getEvent = event.split(",")
    return getEvent

def splitEvent(getEvent):
    eventID= getEvent[0]
    businessID = getEvent[1]
    eventDate= getEvent[2]
    eventCoins= getEvent[3]
    return eventID, businessID, eventDate, eventCoins

def eventsTable(eventID, businessID, eventDate, eventCoins):
    print("<table>")
    print("<tr>")
    print("<th>",'Event ID',"</th>")
    print("<th>",'Business ID',"</th>")
    print("<th>",'Date of event',"</th>")
    print("<th>",'Coins',"</th>")
    print("</tr>")
    print("<tr>")
    print("<td>",str(eventID),"</td>")
    print("<td>",str(businessID),"</td>")
    print("<td>",str(eventDate),"</td>")
    print("<td>",str(eventCoins),"</td>")
    print ("</tr>")
    print("</table>")

def individualMain():
    getIndividual = individualInit()
    customerID, individualName, individualPass, individualCoins, individualEmail = splitIndividual(getIndividual)
    individualsTable(customerID, individualName, individualPass, individualCoins, individualEmail)

def individualInit():
    individual = ("101010, lager benson, password123, 1, lBen@omg.com")
    getIndividual = individual.split(",")
    return getIndividual

def splitIndividual(getIndividual):
    customerID = getIndividual[0]
    individualName = getIndividual[1]
    individualPass= getIndividual[2]
    individualCoins= getIndividual[3]
    individualEmail= getIndividual[4]
    return customerID, individualName, individualPass, individualCoins, individualEmail

def individualsTable(customerID, individualName, individualPass, individualCoins, individualEmail):
    print("<table>")
    print("<tr>")
    print("<th>",'Customer ID',"</th>")
    print("<th>",'Name',"</th>")
    print("<th>",'Password',"</th>")
    print("<th>",'Coins',"</th>")
    print("<th>",'Email',"</th>")
    print("</tr>")
    print("<tr>")
    print("<td>",str(customerID),"</td>")
    print("<td>",str(individualName),"</td>")
    print("<td>",str(individualPass),"</td>")
    print("<td>",str(individualCoins),"</td>")
    print("<td>",str(individualEmail),"</td>")
    print ("</tr>")
    print("</table>")

def businessMain():
    getBusiness = businessInit()
    businessID, businessName, businessPass, businessCoins, businessEmail = splitBusiness(getBusiness)
    businessTable(businessID, businessName, businessPass, businessCoins, businessEmail)

def businessInit():
    business = ("101010, Jackelson Jacks, Kj6p7e0, 99999999999999, jackelson@gmo.com")
    getBusiness = business.split(",")
    return getBusiness

def splitBusiness(getBusiness):
    businessID = getBusiness[0]
    businessName = getBusiness[1]
    businessPass= getBusiness[2]
    businessCoins= getBusiness[3]
    businessEmail= getBusiness[4]
    return businessID, businessName, businessPass, businessCoins, businessEmail

def businessTable(businessID, businessName, businessPass, businessCoins, businessEmail):
    print("<table>")
    print("<tr>")
    print("<th>",'Business ID',"</th>")
    print("<th>",'Business',"</th>")
    print("<th>",'Password',"</th>")
    print("<th>",'Coins',"</th>")
    print("<th>",'Email',"</th>")
    print("</tr>")
    print("<tr>")
    print("<td>",str(businessID),"</td>")
    print("<td>",str(businessName),"</td>")
    print("<td>",str(businessPass),"</td>")
    print("<td>",str(businessCoins),"</td>")
    print("<td>",str(businessEmail),"</td>")
    print ("</tr>")
    print("</table>")

main()














