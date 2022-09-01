from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# webdriver_manager 인스톨 필요
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui as pag
import time

class NewsBot:
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--window-size=1600,900')
        self.driver = webdriver.chrome(service=Service(ChromeDriverManager().install()), chrome_options=self.options)
        self.news_query = f'https://www.google.com/search?tbm=nws&q='
        self.news_list = []
        self.news_text = ''
    
    def search(self, keyword):
        self.driver.get(f'{self.news_query}{keyword}')
        time.sleep(1)
    
    def refresh(self):
        pag.press('f5')
    
    def copy_all(self):
        pag.hotkey('ctrl', 'a')
        time.sleep(1)
        pag.hotkey('ctrl', 'c')
        time.sleep(1)
        pag.hotkey('ctrl', 'c')
    
    def scrap_news(self):
        self.copy_all()
        self.news_list = []
        self.news_text = pyperclip.paste()
        # list로 변환할 때 따옴표 때문에 걸리는게 있어서 모두 큰 따옴표로 전환
        split_text = self.news_text.replace('\'', '"').splitlines()
        