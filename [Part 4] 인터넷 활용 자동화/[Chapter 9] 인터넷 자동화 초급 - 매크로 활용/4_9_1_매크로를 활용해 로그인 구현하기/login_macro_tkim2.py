from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# webdriver_manager 인스톨 필요
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui as pag
import time

LOGIN_URLS = {
    'twitter': 'https://twitter.com/login',
    'daum': 'https://logins.daum.net/accounts/signinform.do',
    'naver' : f'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
}

class LoginBot:
    def __init__(self, site):
        self.options = Options()
        self.options.add_argument('--window-size=1600,900')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=self.options)
        try:
            self.driver.get(LOGIN_URLS[site.lower()])
            time.sleep(1)
        except:
            self.driver.get(site)
            time.sleep(1)
        
    def login(self, id, pw):
        pag.write(id, 0.1)
        pag.write(['tab'])
        pag.write(pw, 0.1)
        pag.write(['enter'])
        time.sleep(1)
    
