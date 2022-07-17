# 필요 라이브러리 전체 수집(bs4, selenium, requests 등)
from bs4 import BeautifulSoup as BS
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import requests
from urllib.request import urlopen

# driver 객체 확인
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# driver.get()활용
url = '실제 url'
driver.get(url)

# page 객체 확인
page = driver.page_source

# page 객체로 bs4 활용
bs_obj = BS(page, 'html.parser')