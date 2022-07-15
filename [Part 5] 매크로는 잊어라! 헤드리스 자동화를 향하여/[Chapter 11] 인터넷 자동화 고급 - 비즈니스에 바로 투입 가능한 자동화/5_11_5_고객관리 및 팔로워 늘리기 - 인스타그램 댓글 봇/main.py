#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.03.02.
"""

import sys
import time
import insta_bot_reply as ib


# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ���� ������ �Էµ� ���� �̸��� �Է¹޽��ϴ�.
id_filename = sys.argv[1]

# �˻��� �±װ� ��ϵ� ������ �Է¹޽��ϴ�.
tag_filename = sys.argv[2]

# ��� ���õ��� �Էµ� ���� �̸��� �Է¹޽��ϴ�.
rep_filename = sys.argv[3]

# ũ�ѷ��� �ҷ��ɴϴ�.
BOT = ib.ReplyBot(rep_filename)

# id ������ �ҷ��ɴϴ�.
id_file = open(id_filename)
# ����Ʈ�� ����� �ݴϴ�.
IDs = []
for line in id_file:
    splt = line.split(",")
    if len(splt) != 2:
        continue
    IDs.append((splt[0].strip(), splt[1].strip()))

# �±� ���ϵ� �ҷ��ɴϴ�.
tag_file = open(tag_filename)

# ����Ʈ�� ����� �ݴϴ�.
Tags = tag_file.read().split("\n")

# ���ѹݺ� �� ������ while True�� �ְ��Դϴ�.
while True:
    # ������ �ϳ��� �ҷ��ɴϴ�.
    for account in IDs:
        # ������ �ٲ������ ����̹��� ���ٰ� �� �ݴϴ�.
        BOT.driver_refresh()
        # �α����� �սô�.
        BOT.login(account)
        # �±׸� �ϳ��� �ҷ��ɴϴ�.
        for tag in Tags:
            # �ҷ��� �±׸� ������� Ž���ϸ� ���ƿ並 �����ϴ�. �Խù��� �� ���� 100������ ���ƿ� ������ ��� ��ϴ�.
            BOT.insta_jungdok(tag, num=100)
        # ������ �ٲ� ������ 1�о� ��ٷ� �ݴϴ�.
        # ������ ����� �ʹ� ���� �Է��ϸ� ���� ���ϱ� �����Դϴ�.
        time.sleep(60)

# ũ�ѷ��� �ݾ��ݴϴ�.
BOT.kill()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
