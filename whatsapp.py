from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome(executable_path=r"C:\Users\nEW u\AppData\Local\Temp\Rar$EXa0.924\chromedriver.exe")

browser.get("https://web.whatsapp.com/")

name = input('Enter name of recipient:')
msg = input('Enter your Message:')
count=input('Enter the Count of messages:')

try:
    elem = browser.find_element_by_class_name('_3Bxar')
    print('Found <%s> element with that class name!' % (elem.tag_name))
except:
    print('Was not able to find an element with that name.')

user = browser.find_element_by_xpath('//span[@title = "{}"]'.format(name))

user

user.click()

try:
    msg_box = browser.find_element_by_class_name('_2S1VP')
    print('Found <%s> element with that class name!' % (msg_box.tag_name))
except:
    print('Was not able to find an element with that name.')

for i in range(int(count)):
    msg_box.send_keys(msg)
    send=browser.find_element_by_class_name('_2lkdt')
    send.click()
