#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.02.12.
"""
import time
import random
import os
import pyexcel as px


# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ������ �������� ���� ������ �����մϴ�.
NUM_SAMPLES = 1000

# �̸��� ������ ����� ���� ���ڵ��� �����մϴ�.
alphabet_samples = "abcdefghizklmnopqrstuvwxyz1234567890"


# �������� ���õ� ���� ���ڸ� �����ϴ� �Լ��Դϴ�.
def random_string(length):
    result = ""
    for i in range(length):
        result += random.choice(alphabet_samples)
    return result


# �̸� ������ ����� ���� ���ڵ��� �����մϴ�.
first_name_samples = "���̹���������������"
middle_name_samples = "�μ�������������ä����"
last_name_samples = "�������ȣ�ļ���������"


# �������� ��� �̸��� �����ϴ� �Լ��Դϴ�.
def random_name():
    result = ""
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result


# ������� ������ ������ �����մϴ�.
os.mkdir("personal_info")

# ����� �����մϴ�.
HEADER = ["name", "age", "e-mail", "division", "telephone", "sex"]


# �������� ������ �ڵ����� �����ϴ� �κ��Դϴ�.
# NUM_SAMPLES ȸ����ŭ �ݺ��մϴ�.
# �̸��׸�, NUM_SAMPLES�� 100�̸� ������ �������� ������ 100ȸ �ݺ��մϴ�.
for i in range(NUM_SAMPLES):
    # �������� ��� �̸��� �����մϴ�.
    name = random_name()

    # ����� ������ �̸��� �����մϴ�.
    filename = "personal_info/" + str(i) + "_" + name + ".xlsx"

    # �������Ϸ� ������ �����͸� ��� �� ����Ʈ�� ����ϴ�.
    contents = []

    # �̸��� �����մϴ�.
    contents.append(name)

    # �������� ������ ���̸� �����մϴ�.
    contents.append(str(time.time())[-2:])

    # �������� ������ �̸����� �����մϴ�.
    contents.append(random_string(8) + "@bhban.com")

    # �������� ������ �μ����� �����մϴ�.
    contents.append(random_string(3))

    # �������� ������ �ڵ��� ��ȣ�� �����մϴ�.
    contents.append("010-" + str(time.time())[-4:] + "-" + str(time.time())[-6:-2])

    # �������� ������ ������ �����մϴ�.
    contents.append(random.choice(["male", "female"]))

    # ����� �����͸� ���ļ� ������ �����͸� �ϼ��մϴ�.
    RESULT = [HEADER, contents]

    # �ϼ��� ���������� �����մϴ�.
    px.save_as(array=RESULT, dest_file_name=filename)

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
