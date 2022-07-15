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

# �ϳ��� ��ĥ ���ϵ��� ����� ���� �̸��� �ý������κ��� �Է¹޽��ϴ�.
directory = sys.argv[1]

# ���� ����� ���� �̸��� �����մϴ�.
outfile_name = "merged_ID.xlsx"

# ������ ���빰�� ������ ����� �����մϴ�.
input_files = os.listdir(directory)

# �����Ͱ� ����� ����Ʈ�� ����ϴ�.
CONTENTS = []

# ����� ������ ����Ʈ�� ����ϴ�.
HEADERS = []

# ��� �Է��� ���� �Ҹ��� ������ ����ϴ�.
contents_has_header = False

# ������ ���빰�� �ϳ��ϳ� �ҷ��� ��ġ�� �۾��� �����մϴ�.
# input_files�� ����� ���� �̸��� �� ���� �ϳ��� �ҷ��ɴϴ�.
for filename in input_files:
    # ��Ȥ �ؽ�Ʈ ������ �ƴ� ������ �������� �� �ֽ��ϴ�. �̰� �ɷ����ϴ�.
    if ".txt" not in filename:
        continue

    # �ؽ�Ʈ ������ �´ٸ�, ������ �о�ɴϴ�.
    file = open(directory + "/" + filename)

    # ������ ������ ����Ʈ�� ����ϴ�.
    contents = []

    # ������ ���빰�� �� �پ� �о���鼭 �۾��� �����մϴ�.
    for line in file:
        # ����� �߸��� ������ �����ϴ�.
        if " : " not in line:
            continue

        # �ؽ�Ʈ������ ����� ���빰�� �и��մϴ�.
        header, content = line.strip().split(" : ")

        # ���� ����� �Էµ��� �ʾҴٸ� ����� ����ϴ�.
        # �� �ڵ�� ó�� �� ���� ���Ͽ����� ����˴ϴ�.
        if not contents_has_header:
            HEADERS.append(header)

        # �о�� �����͸� �����մϴ�.
        contents.append(content)

    # ���� ����� �Էµ��� �ʾҴٸ� ����� �Է��մϴ�.
    # �� �ڵ�� �� ���� ����˴ϴ�.
    if not contents_has_header:
        CONTENTS.append(HEADERS)
        contents_has_header = True

    # CONTENTS �� ����� ���빰�� �Է��մϴ�.
    CONTENTS.append(contents)

    # �о�� ������ �����մϴ�.
    file.close()

# CONTENTS�� ����� �ڷḦ �������Ϸ� ����մϴ�.
px.save_as(array=CONTENTS, dest_file_name=outfile_name)

# �۾� ���� �޽����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")