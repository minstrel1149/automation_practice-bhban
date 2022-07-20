from ast import keyword
import sys
import time
import excel_bot_news_tkim1 as eb

keyword = sys.argv[1]
page_number = sys.argv[2]
filename = sys.argv[3]

BOT = eb.NewsBot()
BOT.news_search(keyword, page_number)
BOT.to_excel(filename)

BOT.kill()

print('Process Done!')