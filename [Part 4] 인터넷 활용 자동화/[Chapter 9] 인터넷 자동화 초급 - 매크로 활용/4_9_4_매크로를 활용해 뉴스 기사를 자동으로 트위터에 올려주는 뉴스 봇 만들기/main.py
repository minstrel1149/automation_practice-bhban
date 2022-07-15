#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.03.02.
"""

import sys
import time
import twitter_bot_news as tb


# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ���̵� �Է¹޽��ϴ�.
id = sys.argv[1]

# �н����带 �Է¹޽��ϴ�.
ps = sys.argv[2]

# �˻�� �Է¹޽��ϴ�.
keyword = sys.argv[3].strip()

# ũ�ѷ��� �ҷ��ɴϴ�.
BOT = tb.NewsBot()

# �α����� �õ��մϴ�.
BOT.login(id, ps)

# ������ �Բ� ������ �ؽ��±׸� �Է��մϴ�.
hashtags = "#���� #��ũ�� �ϴ� #�ڵ�ȭ #�ڵ�"

# ���ۿ��� ������ �˻��ϰ�,
# Ʈ���Ϳ� �ڵ����� �α��� �� ��,
# �ܾ�� ��� ������ ���ε���� �մϴ�.
BOT.tweet_all_news(keyword, hashtags)

# ��� ȭ���� ��� �����ϱ� ���� 10�ʵ��� ��ġ�մϴ�.
time.sleep(10)

# ũ�ѷ��� �ݾ��ݴϴ�.
BOT.kill()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
