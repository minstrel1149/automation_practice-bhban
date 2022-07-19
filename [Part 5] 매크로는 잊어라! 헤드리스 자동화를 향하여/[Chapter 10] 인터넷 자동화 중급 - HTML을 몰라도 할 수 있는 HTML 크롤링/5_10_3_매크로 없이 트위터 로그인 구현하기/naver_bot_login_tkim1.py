from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# webdriver_manager 인스톨 필요
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

class LoginBot:
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--window-size=1600,900')
        # 헤드리스는 일단 주석처리
        # self.options.add_argument('headless')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=self.options)

    def kill(self):
        self.driver.quit()
    
    def login(self, id, pw):
        self.driver.get(f'https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')
        time.sleep(2)
        # 키워드 전달인자 다음에 위치 전달인자는 사용 불가 -> 둘 다 위치 전달인자로 구성해야
        # 과거 형태 대신 driver.find_element(By.xxx, 'xxxx') 형태 활용
        id_input = self.driver.find_element(By.NAME, 'id')
        id_input.send_keys(id)
        pw_input = self.driver.find_element(By.NAME, 'pw')
        pw_input.send_keys(pw)
        pw_input.submit()