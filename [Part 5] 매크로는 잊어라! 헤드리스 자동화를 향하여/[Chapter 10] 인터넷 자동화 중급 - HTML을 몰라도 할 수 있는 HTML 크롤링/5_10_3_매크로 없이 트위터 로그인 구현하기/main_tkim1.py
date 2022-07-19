import sys
import time
import naver_bot_login_tkim1 as nb

print("Process Start.")

id = sys.argv[1]
pw = sys.argv[2]

BOT = nb.LoginBot()
BOT.login(id, pw)

time.sleep(10)

BOT.kill()

print("Process Done!")