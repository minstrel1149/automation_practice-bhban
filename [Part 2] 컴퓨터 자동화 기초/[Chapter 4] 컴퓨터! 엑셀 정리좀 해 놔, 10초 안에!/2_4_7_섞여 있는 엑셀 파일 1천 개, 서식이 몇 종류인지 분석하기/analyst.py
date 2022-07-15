#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.02.12.
"""
import time
import os
import pyexcel as px
import sys

# �۾� ���� �޽����� ����մϴ�.
print("Process Start")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ���ϵ��� ����� ���� �̸��� �ý������κ��� �Է¹޽��ϴ�.
directory = sys.argv[1]

# �м� ��� ���� �̸��� �ý������κ��� �Է¹޽��ϴ�.
report_filename = sys.argv[2]

# ������ ���빰�� ������ ����� �����մϴ�.
input_files = os.listdir(directory)

# ������� ������ ��ųʸ��� ����ϴ�.
HEADERS = {}

# input_files�� ����� ���� �̸��� �� ���� �ϳ��� �ҷ��ɴϴ�.
# ����� �� �������� �м��մϴ�.
for filename in input_files:
    # ��Ȥ xlsx ������ �ƴ� ������ �������� �� �ֽ��ϴ�. �̰� �ɷ����ϴ�.
    if ".xlsx" not in filename:
        continue

    # ���� ������ �´ٸ�, ������ ����Ʈ ���·� �о�ɴϴ�.
    file = px.get_array(file_name=directory + "/" + filename)

    # ���� ������ ù ��° ��, �׷��ϱ� ����� �ҷ��� ��Ʈ������ ��ȯ�մϴ�.
    header = str(file[0])

    # ��ųʸ��� ����� ���ԵǾ� �ִ��� Ȯ���մϴ�.
    if header in HEADERS:
        # �̹� ���ԵǾ� �ִٸ� ���� 1�� ������ŵ�ϴ�.
        HEADERS[header] += 1
    else:
        HEADERS[header] = 1

# ����� ����Ʈ�� �ۼ��ϱ� ���� ��Ʈ���� �����մϴ�.
REPORT = ""

# ����Ʈ�� ���빰�� �ڵ����� �ۼ��մϴ�.
for key in HEADERS:
    REPORT += "Header : " + key + "\n"
    REPORT += "Count : " + str(HEADERS[key]) + "\n\n"

# ����Ʈ�� ȭ�鿡 ����մϴ�.
print(REPORT)

# ����Ʈ ���Ͽ� ����Ʈ�� �����մϴ�.
report_file = open(report_filename, 'w')
report_file.write(REPORT)
report_file.close()

# �۾� ���� �޽����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
