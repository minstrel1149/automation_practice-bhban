import sys
import time
import excel_bot_news_tkim2 as eb

keyword = sys.argv[1].strip()
filename = sys.argv[2]

Bot = eb.NewsBot()
Bot.news_crawler(keyword)
Bot.to_excel(filename)

print('Process Done!')