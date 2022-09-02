from fileinput import filename
import sys
import time
import excel_bot_news_tkim2 as eb

keyword = sys.argv[1]
number = sys.argv[2]
filename = sys.argv[3]

excel_news = eb.NewsBot()
excel_news.news_search(keyword, number)
excel_news.to_excel(filename)

print('Process Done!')