from selenium import webdriver
import time
from twilio.rest import Client

account_SID = 'ACe8d5aab8344b1a01366b690244b2fa9e'
auth_token = 'd907e4b9f11a1f807d82a92c31f3bc38'
my_number = '+8617610780955'
twilio_number = '+12566074275'


def text_myself(message):
    twilio_client = Client(account_SID, auth_token)

    twilio_client.messages.create(body=message, from_=twilio_number, to=my_number)


def get_VBCCNY():
    browser = webdriver.Chrome()
    browser.get('https://c.radarlab.org/markets/VBCCNY')
    while True:
        r = browser.find_element_by_css_selector('i[code=CNY]')
        print(r.text)
        time.sleep(1)


text_myself("helloLCT")
