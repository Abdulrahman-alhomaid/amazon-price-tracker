from selenium import webdriver
import time
import smtplib
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse, Say


def main():
    #driver = webdriver.Chrome('chromedriver.exe') #
    driver = webdriver.PhantomJS('phantomjs.exe')
    price = []
    links = []
    products = []
    with open('wbeScrapingProducts.txt','r') as f:
        for line in f:
            contant = line.split(",")
            links.append(contant[0])
            price.append(contant[1])


    discoundProducts = []
    for i in range(len(links)):
 
        driver.get(links[i])
        
        try:
            title = driver.find_element_by_id('productTitle').get_attribute('innerHTML')     
            productPrice = driver.find_element_by_id('priceblock_ourprice').get_attribute('innerHTML')
            fPrice = productPrice[1:].replace(',' , '')
        
            if float(price[i]) > float(fPrice):
                discoundProducts.append(title.strip())
                discoundProducts.append(fPrice)
                discoundProducts.append(links[i])
                print('got one')
        except Exception:
            print(links[i])    
    if len(discoundProducts) > 0:
        print('sending email')
        sendEmail(discoundProducts)
        # makeCall()
    else:
        print('did not find any')    
        #time.sleep(21600)

def sendEmail(discoundProducts):
    email = 'EMAIL HERE'
    msg = '\n\n\n'
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(email , 'osmjdlndlloplfwg')
    end = len(discoundProducts)
    #print(end)
    for i in range(0 , end , 3 ):
        #print(discoundProducts[i])
        msg += 'price is down for ' + str(discoundProducts[i]) + ' ,it is now sells for ' + str(discoundProducts[i+1]) + '$ check the link => '+ str(discoundProducts[i+2]) + '\n\n'
        
        #print('--------------------------------------------')
    #print(msg)    
    server.sendmail(email, email , msg)
    print('mail sent')

    server.quit()    

def makeCall():
    account_sid = 'twilio account sid'
    auth_token = 'twilio auth_token'
    clint = Client(account_sid , auth_token)
    call = clint.calls.create( to='+966553615535' ,from_='+18776121508' , url='https://43a67528.ngrok.io/voice')
    print(call.sid)

main()