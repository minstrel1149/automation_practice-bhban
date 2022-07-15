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

# �۾� ���� �޽����� ����մϴ�.
print("Process Start")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ������ �м��� ��ĥ ���ϵ��� ����� ���� �̸��� �ý������κ��� �Է¹޽��ϴ�.
directory = sys.argv[1]

# ������� ������ ������ �����մϴ�.
out_dir ="merged_" + directory
if out_dir not in os.listdir():
    os.mkdir(out_dir)

# ������ ���빰�� ������ ����� �����մϴ�.
input_files = os.listdir(directory)

# ������� ������ ����Ʈ�� ����ϴ�.
HEADERS = []

# ���� ������� ������ ����Ʈ�� ����ϴ�.
CONTENTS = []

# input_files�� ����� ���� �̸��� �� ���� �ϳ��� �ҷ��ɴϴ�.
for filename in input_files:
    # ��Ȥ xlsx ������ �ƴ� ������ �������� �� �ֽ��ϴ�. �̰� �ɷ����ϴ�.
    if ".xlsx" not in filename:
        continue

    # ���� ������ �´ٸ�, ������ ����Ʈ ���·� �о�ɴϴ�.
    file = px.get_array(file_name=directory + "/" + filename)

    # ���� ������ ù ��° ��, �׷��ϱ� ����� �ҷ��ɴϴ�.
    header = file[0]
    content = file[1:]

    # �ҷ��� ������ ����� �̹� �о�Դ� ���ϰ� ��ġ�ϴ��� �м��մϴ�.
    # �Ʒ� �ڵ�� ���ο� ����� �߰ߵ� ������ �۵��մϴ�.
    if header not in HEADERS:
        # ó�� �߰ߵ� ������ ����� �Ӵϴ�.
        HEADERS.append(header)
        # ����� ���� ���ø� ����Ʈ�� �����Ͽ� ������ �Ӵϴ�.
        CONTENTS.append([header])

    # ������ ���� ����Ʈ�� �ҷ��ɴϴ�.
    index = HEADERS.index(header)

    # ����Ʈ�� ������ ���� �Է��մϴ�.
    CONTENTS[index] += content

# ������ �����͵��� ���� ���� ���Ϸ� �����մϴ�.
for i in range(len(CONTENTS)):
    px.save_as(array=CONTENTS[i], dest_file_name=out_dir + "/" + str(i) + "_merged_File.xlsx")

# �۾� ���� �޽����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
