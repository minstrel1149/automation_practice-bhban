from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

LOGIN_URLS = {
    'twitter': 'https://twitter.com/login',
    'daum': 'https://logins.daum.net/accounts/signinform.do',
    'naver' : f'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com'
}

class LoginBot():
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--window-size=1600,900')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=self.options)

    def login(self, site, id, pw):
        if site.lower() in LOGIN_URLS.keys():
            self.driver.get(LOGIN_URLS[site.lower()])
            time.sleep(1)
        else:
            self.driver.get(site)
            time.sleep(1)
        id_input = self.driver.find_element(By.NAME, 'id')
        id_input.send_keys(id)
        pw_input = self.driver.find_element(By.NAME, 'pw')
        pw_input.send_keys(pw)
        pw_input.submit()