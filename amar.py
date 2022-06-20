import smtplib
import selTest
import sendEmail
import time
from email.message import EmailMessage
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

runNum=1
while True:
    amarnathHomePage="http://www.shriamarnathjishrine.com/"

    uClient=uReq(amarnathHomePage)
    page_html=uClient.read()
    uClient.close()

    page_soup=soup(page_html,"html.parser")

    containers = page_soup.findAll("div",{"class":"helicopterDetails"})
    container=containers[0]
    webString=container.h4.text
    validationString='To be updated soon'

    print("Run : "+str(runNum))
    runNum+=1
    
    to = 'koabhifino@gmail.com,deepaksai2000@gmail.com,abko27700@gmail.com'
    subject='URGENT!! AMARNATH UPDATE!!!'
    body='Bookings have started!. Go to'+amarnathHomePage

    contact1 = "Daddy"
    contact2 = "Birthgiver"
    message = "Amarnath Helicopter Booking Has Started! "+"Go to "+amarnathHomePage
    if validationString in webString:
        count=0
        while count<10:
            if count==7:
                to+=',bs.abhishek.kothari@oracle.com'
            sendEmail.email_alert(to,subject,body)
            count+=1
            selTest.whatsapp_message(contact1,message)
            time.sleep(10)
            selTest.whatsapp_message(contact2,message)
            time.sleep(300)
        break
    #else:
    #    selTest.whatsapp_message(contact1,message)
    #    time.sleep(10)
    #    selTest.whatsapp_message(contact2,message)
    time.sleep(300)
    


