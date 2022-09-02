import sys
import naver_bot_login_tkim2 as nb
import time

site = sys.argv[1]
id = sys.argv[2]
pw = sys.argv[3]

login_bot = nb.LoginBot()
login_bot.login(site, id, pw)

print('Process Done!')