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