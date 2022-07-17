import sys
import time
import login_macro_tkim1 as lm

site = sys.argv[1]
id = sys.argv[2]
pw = sys.argv[3]

crawler = lm.LoginBot(site)
crawler.login(id, pw)

crawler.save_screenshot()

print('Process Done!')