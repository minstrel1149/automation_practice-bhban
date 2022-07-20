from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as BS
import pyautogui as pag
import time
import pyperclip
from pathlib import Path
import openpyxl
from openpyxl.styles import Font
from openpyxl.styles import Alignment

# jupyter notebook에서 일단 먼저 실험하는 중 - BeautifulSoup와 Selenium의 연계로
# BeautifulSoup와 Selenium의 연계로 나만의 코드로 진행

class NewsBot():
    def __init__(self):
        self.options = Options()
        self.options.add_argument('--window-size=1600,900')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=self.options)
        self.news_list = []
        self.news_query = 'https://www.google.com/search?tbm=nws&q='

    def kill(self):
        self.driver.quit()

    def news_search(self, keyword):
        self.news_list = []
        self.driver.get(self.news_query + keyword)
        self.page = self.driver.page_source
        self.bs_obj = BS(page, 'html.parser')
        self.news_obj = self.bs_obj.find_all('div', {'class':'xuvV6b BGxR7d'})
        for i, news in enumerate(self.news_obj):
            self.news_company = self.news_obj[i].find('div', {'class':'CEMjEf NUnG9d'}).text
            self.news_title = self.news_obj[i].find('div', {'class':'mCBkyc y355M ynAwRc MBeuO nDgy9d'}).text.replace('\'', '"')
            self.news_summary = self.news_obj[i].find('div', {'class':'GI74Re nDgy9d'}).text.replace('\n', '').replace('\'', '"')
            self.news_period = self.news_obj[i].find('div', {'class':'OSrXXb ZE0LJd'}).text
            self.news_list.append([self.news_company, self.news_title, self.news_summary, self.news_period])

    def page_crawling(self, number):
        for i in range(int(number)):
            self.news_search(self, keyword)
            self.html_element = self.driver.find_element(By.TAG_NAME, 'html')
            self.html_element.send_keys(Keys.END)
            time.sleep(1)
            self.next_link = self.driver.find_element(By.LINK_TEXT, '다음')
            self.next_link.click()

# 아직 작성중.. news_search와 page_crawling을 다시 결합해야할 것 같은 느낌..