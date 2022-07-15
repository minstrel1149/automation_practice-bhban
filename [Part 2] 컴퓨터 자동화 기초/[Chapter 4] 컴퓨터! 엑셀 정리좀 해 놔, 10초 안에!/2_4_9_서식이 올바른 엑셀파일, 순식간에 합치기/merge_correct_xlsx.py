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

# ���� ���÷� ����� ���� �̸��� �ý������κ��� �Է¹޽��ϴ�.
template = sys.argv[1]

# ���ϵ��� ����� ���� �̸��� �ý������κ��� �Է¹޽��ϴ�.
directory = sys.argv[2]

# ������ ���빰�� ������ ����� �����մϴ�.
input_files = os.listdir(directory)

# ���ø� ������ �о�� ����� �и��մϴ�.
HEADER = px.get_array(file_name=template)[0]

# �����͸� ������ ����Ʈ�� ����ϴ�. ����� �־��ݴϴ�.
CONTENTS = [HEADER]

# input_files�� ����� ���� �̸��� �� ���� �ϳ��� �ҷ��ɴϴ�.
for filename in input_files:
    # ��Ȥ xlsx ������ �ƴ� ������ �������� �� �ֽ��ϴ�. �̰� �ɷ����ϴ�.
    if ".xlsx" not in filename:
        continue

    # ���� ������ �´ٸ�, ������ ����Ʈ ���·� �о�ɴϴ�.
    file = px.get_array(file_name=directory + "/" + filename)

    # ���� ������ ù ��° ��, �׷��ϱ� ����� �ҷ��ɴϴ�.
    header = file[0]

    # �ҷ��� ������ ����� ���ø��� ��ġ�ϴ��� �м��մϴ�.
    if HEADER != header:
        # ��ġ���� �ʴ´ٸ� �ǳʶپ�����ô�
        continue

    # CONTENTS ����Ʈ�� ���� ������ ���빰�� �Է��մϴ�.
    CONTENTS += file[1:]

# ������ ���� ������ �����մϴ�.
px.save_as(array=CONTENTS, dest_file_name="merged_FILE.xlsx")

# �� ��� ������ ������������ ����մϴ�.
print("Total " + str(len(CONTENTS) - 1) + " files were merged.")

# �۾� ���� �޽����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
