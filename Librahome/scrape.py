from selenium import webdriver
from selenium.webdriver.chrome.options import Options
#from pyvirtualdisplay import Display
import datetime
import time
import schedule
import os


#display = Display(visible=0, size = (1280, 760))
#display.start()
path = './static/screenshot'

def showtime():
    timenow = str((datetime.datetime.now()))
    timenow = timenow.replace(' ','_')
    timenow = timenow.replace('-', '_')
    timenow = timenow.replace(':', '_')
    return timenow

def find_screenshot():
    screenshot = [f for f in os.listdir(path) if f.endswith('CNN.png')]
    screenshot.sort()
    print(screenshot)
#find_screenshot()

options =Options()
options.add_argument("--headless")
options.add_argument("--window-size=1920,1080")
options.add_argument('--no-sandbox')

def cnn():
    #os.system(
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=options, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
    driver.get('http://cnn.com')
    driver.save_screenshot("./static/screenshot/{time}CNN.png".format(time=showtime()))
    driver.close()
    #display.stop
#cnn()

def nbc():
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=options, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
    #driver = webdriver.Chrome("/mnt/c/Users/TheOn/AppData/Local/Programs/Python/Python36-32/selenium/webdriver/chromedriver_win32/chromedriver.exe")
    driver.get('http://nbcnews.com')
    driver.save_screenshot("./static/screenshot/{time}NBC.png".format(time=showtime()))
    driver.close()
#nbc()

def fox():
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=options, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
    #driver = webdriver.Chrome("/mnt/c/Users/TheOn/AppData/Local/Programs/Python/Python36-32/selenium/webdriver/chromedriver_win32/chromedriver.exe")
    driver.get('http://foxnews.com')
    driver.save_screenshot("./static/screenshot/{time}FOX.png".format(time= showtime()))
    driver.close()
#fox()

def nydailynews():
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=options, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
    #driver = webdriver.Chrome("/mnt/c/Users/TheOn/AppData/Local/Programs/Python/Python36-32/selenium/webdriver/chromedriver_win32/chromedriver.exe")
    driver.get('http://nydailynews.com')
    driver.save_screenshot("./static/screenshot/{time}NYDAILYNEWS.png".format(time= showtime()))
    driver.close()
#nydailynews()

def abc():
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=options, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
    #driver = webdriver.Chrome("/mnt/c/Users/TheOn/AppData/Local/Programs/Python/Python36-32/selenium/webdriver/chromedriver_win32/chromedriver.exe")
    driver.get('http://abcnews.go.com')
    driver.save_screenshot("./static/screenshot/{time}ABC.png".format(time= showtime()))
    driver.close()
#abc()

def washingtonpost():
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=options, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
    #driver = webdriver.Chrome("/mnt/c/Users/TheOn/AppData/Local/Programs/Python/Python36-32/selenium/webdriver/chromedriver_win32/chromedriver.exe")
    driver.get('http://washingtonpost.com')
    driver.save_screenshot("./static/screenshot/{time}WASHINGTONPOST.png".format(time= showtime()))
    driver.close()
#washingtonpost()

def nytimes():
    driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', chrome_options=options, service_args=['--verbose', '--log-path=/tmp/chromedriver.log'])
    #driver = webdriver.Chrome("/mnt/c/Users/TheOn/AppData/Local/Programs/Python/Python36-32/selenium/webdriver/chromedriver_win32/chromedriver.exe")
    driver.get('http://nytimes.com')
    driver.save_screenshot("./static/screenshot/{time}NEWYORKTIMES.png".format(time= showtime()))
    driver.close()
#nytimes()



schedule.every(6).hours.do(showtime)
#schedule.every().day.at("07:00").do(cnn,nbc,fox)
schedule.every(6).hours.do(cnn)
schedule.every(6).hours.do(nbc)
schedule.every(6).hours.do(fox)
schedule.every(6).hours.do(abc)
schedule.every(6).hours.do(washingtonpost)
schedule.every(6).hours.do(nydailynews)
schedule.every(6).hours.do(nytimes)



while True:
    schedule.run_pending()
    time.sleep(1)
