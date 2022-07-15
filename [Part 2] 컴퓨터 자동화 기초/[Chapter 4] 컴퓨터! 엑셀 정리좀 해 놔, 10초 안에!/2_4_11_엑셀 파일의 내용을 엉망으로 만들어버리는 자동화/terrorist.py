#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.02.13.
"""
import time
import os
import pyexcel as px
import sys
import random

# �۾� ���� �޽����� ����մϴ�.
print("Process Start")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ������ �����߸� ���ϵ��� ����� ���� �̸��� �ý������κ��� �Է¹޽��ϴ�.
directory = sys.argv[1]

# �� �ۼ�Ʈ�� �����͸� �����߸� ������ �ý������κ��� �Է¹޽��ϴ�.
percent = float(sys.argv[2])/100

# ������ ���빰�� ������ ����� �����մϴ�.
input_files = os.listdir(directory)

# ���� �ִ� �ڷ� ��� ������� ������� �ܾ���� ����ݴϴ�.
TERROR = ["�����", "�߿�", "�߿���", "�̾߿�", "����Ի���ؿ�"]

# input_files�� ����� ���� �̸��� �� ���� �ϳ��� �ҷ��ɴϴ�.
for filename in input_files:
    # ��Ȥ xlsx ������ �ƴ� ������ �������� �� �ֽ��ϴ�. �̰� �ɷ����ϴ�.
    if ".xlsx" not in filename:
        continue

    # ���� ������ �´ٸ�, ������ ����Ʈ ���·� �о�ɴϴ�.
    data = px.get_array(file_name=directory + "/" + filename)

    # ���� ������ �����մϴ�.
    os.remove(directory + "/" + filename)

    # 2�� for������ �����Ϳ� �����մϴ�.
    for i in range(len(data)):
        for j in range(len(data[i])):
            # �ı� Ȯ���� �����մϴ�.
            if random.random() < percent:
                # Ȯ���� ��÷�� �Ǿ��ٸ� �����͸� �ı��մϴ�.
                data[i][j] = random.choice(TERROR)

    # ������ �Ϸ�� ���Ϸ� �ٲ�ġ���մϴ�.
    px.save_as(array=data, dest_file_name=directory + "/" + filename)

# �۾� ���� �޽����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
