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

# ����� ������ �̸��� �����մϴ�.
outfile_name = "merged_ID.xlsx"

# ������ ���빰�� ������ ����� �����մϴ�.
input_files = os.listdir(directory)

# �������Ͽ� �� ���빰�� ����� ����Ʈ�� ����ϴ�.
CONTENTS = []

# ������ ���빰�� �ϳ��ϳ� �ҷ��� ��ġ�� �۾��� �����մϴ�.
# input_files�� ����� ���� �̸��� �� ���� �ϳ��� �ҷ��ɴϴ�.
for filename in input_files:
    # ��Ȥ xlsx ������ �ƴ� ������ �������� �� �ֽ��ϴ�. �̰� �ɷ����ϴ�.
    if ".xlsx" not in filename:
        continue

    # ���� ������ �´ٸ�, ������ ����Ʈ ���·� �о�ɴϴ�.
    data_array = px.get_array(file_name=directory + "/" + filename)

    # ����� �и��մϴ�.
    header = data_array[0]
    data_array = data_array[1:]

    # ����� �Է��մϴ�. ���� 1ȸ�� ����˴ϴ�.
    if len(CONTENTS) == 0:
        CONTENTS.append(header)

    # ������� ���빰�� �Է��մϴ�.
    CONTENTS += data_array

# �ϼ��� ���������� �����մϴ�.
px.save_as(array=CONTENTS, dest_file_name=outfile_name)

# �۾� ���� �޽����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
