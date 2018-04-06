from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import datetime
import time
import os

path = '/mnt/c/Users/TheOn/Documents/Libranews/Librahome/Librahome/static/screenshot'
timenow = str((datetime.datetime.now()))
timenow = timenow.replace(' ','_')
timenow = timenow.replace('-', '_')
timenow = timenow.replace(':', '_')
print(timenow)

def find_screenshot():
    screenshot = [f for f in os.listdir(path) if f.endswith('CNN.png')]
    print(screenshot)
find_screenshot()


option = Options()
option.add_argument("--headless")
#option.add_argument("--window-size=1280x760")
option.add_argument('--no-sandbox')

def cnn():
    driver = webdriver.Chrome(chrome_options=option, executable_path="/mnt/c/Users/TheOn/AppData/Local/Programs/Python/Python36-32/selenium/webdriver/chromedriver_win32/chromedriver.exe", service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
    driver.get('http://cnn.com')
    driver.save_screenshot("/mnt/c/Users/TheOn/Documents/Libranews/Librahome/Librahome/static/screenshot/{time}CNN.png".format(time=timenow))
    driver.close()
cnn()

def nbc():
    driver = webdriver.Chrome(chrome_options=option, executable_path="/mnt/c/Users/TheOn/AppData/Local/Programs/Python/Python36-32/selenium/webdriver/chromedriver_win32/chromedriver.exe", service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
    driver.get('http://nbcnews.com')
    driver.save_screenshot("/mnt/c/Users/TheOn/Documents/Libranews/Librahome/Librahome/static/screenshot/{time}NBC.png".format(time=timenow))
    driver.close()
nbc()

def fox():
    driver = webdriver.Chrome(chrome_options=option, executable_path="/mnt/c/Users/TheOn/AppData/Local/Programs/Python/Python36-32/selenium/webdriver/chromedriver_win32/chromedriver.exe", service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
    driver.get('http://foxnews.com')
    driver.save_screenshot("/mnt/c/Users/TheOn/Documents/Libranews/Librahome/Librahome/static/screenshot/{time}FOX.png".format(time= timenow))
    driver.close()
fox()
