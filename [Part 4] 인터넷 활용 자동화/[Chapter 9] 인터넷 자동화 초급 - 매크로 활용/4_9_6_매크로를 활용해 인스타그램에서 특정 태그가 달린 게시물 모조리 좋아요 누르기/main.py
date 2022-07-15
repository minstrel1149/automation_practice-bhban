#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.03.02.
"""

import sys
import time
import insta_bot_like as ib


# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ���̵� �Է¹޽��ϴ�.
id = sys.argv[1]

# �н����带 �Է¹޽��ϴ�.
ps = sys.argv[2]

# �˻��� �±׸� �Է¹޽��ϴ�.
tag = sys.argv[3]

# ���ƿ� ��ư �����̸��� �Է¹޽��ϴ�.
like_button = sys.argv[4]

# ������ ���ƿ� ��ư �����̸��� �Է¹޽��ϴ�.
red_like_button = sys.argv[5]

# �ݺ� ȸ���� �Է¹޽��ϴ�.
NUMBER = int(sys.argv[6].strip())

# ũ�ѷ��� �ҷ��ɴϴ�.
BOT = ib.LikeBot(like_button, red_like_button)

# �ν�Ÿ�׷� �α����� �մϴ�.
BOT.login(id, ps)

# �۾��� �����մϴ�.
BOT.insta_jungdok(tag, NUMBER)

# ũ�ѷ��� �ݾ��ݴϴ�.
BOT.kill()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
