from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
# webdriver_manager 인스톨 필요
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui as pag
import time
import pyperclip
from pathlib import Path
import openpyxl

class NewsBot:
    def __init__(self):
        self.news_query = 'https://www.google.com/search?tbm=nws&q='
        self.options = Options()
        self.options.add_argument('--window-size=1600,900')
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), chrome_options=self.options)
        self.news_list = []
        self.news_text = ''
    def quit_bot(self):
        self.driver.quit()
    def search(self, keyword):
        # 문자열을 합쳐줄 수 있는 '+'로 처리해야함을 잊지 말기
        self.driver.get(self.news_query + keyword)
        time.sleep(2)
    def refresh(self):
        # pyautogui 활용
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
        split_text = self.news_text.splitlines()
        for i, line in enumerate(split_text):
            if len(line.strip()) < 3:
                continue
            elif line.strip()[-3:] in '달 전 주 전 일 전 시간 전 분 전 초 전':
                # 엑셀에 저장할 것이기 때문에 join으로 합치지 말고 list 형태로 진행해야하는데..
                new_news = '\n'.join(split_text[i-3:i])
                self.news_list.append(new_news)
    def news_crawler(self, keyword):
        self.search(keyword)
        self.scrap_news()
    def to_excel(self, filename):
        wb = openpyxl.Workbook()
        wb.create_sheet('Sheet')
        sheet = wb.active
        for i, news in enumerate(self.news_list):
            # i+1 기재해줘야함을 헷갈리지 말고 처리해야
            sheet.cell(i+1, 1).value = news
        wb.save(Path.cwd() / f'{filename}.xlsx')
