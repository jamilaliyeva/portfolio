# from selenium.webdriver.chrome.options import Options
# from selenium import webdriver
# import time
#
# chrome_options = Options()
# chrome_options.add_argument("--user-data-dir=chrome-data")
# driver = webdriver.Chrome(options=chrome_options)
# chrome_options.add_argument("user-data-dir=chrome-data")
# driver.get('https://veto-real.online/sign-in')
# time.sleep(30)
#
# chrome_options = Options()
# chrome_options.add_argument("--user-data-dir=chrome-data")
# driver = webdriver.Chrome(options=chrome_options)
# driver.get('https://veto-real.online/sign-in')  # Already authenticated
# time.sleep(10)
# driver.quit()
from selenium.webdriver.chrome.webdriver import WebDriver

import loginPage
from selenium import webdriver
import json


def saveCookies():
    driver = webdriver.Chrome()
    driver.get("https://veto-real.online/sign-in")
    cookies = driver.get_cookies()
    with open('cookies.json', 'w') as file:
        json.dump(cookies, file)


def loadCookies():
    driver = webdriver.Chrome()
    driver.get("https://veto-real.online/")
    with open('cookies.json', 'r') as file:
        cookies = json.load(file)
    for cookie in cookies:
        driver.add_cookie(cookie)
    driver.refresh()



