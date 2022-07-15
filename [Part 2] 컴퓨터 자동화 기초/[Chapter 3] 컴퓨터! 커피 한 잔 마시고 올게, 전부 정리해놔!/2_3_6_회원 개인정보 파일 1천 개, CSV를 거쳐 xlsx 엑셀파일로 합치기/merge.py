#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.02.12.
"""
import time
import os
import pyexcel.cookbook as PC
import sys

# �۾� ���� �޽����� ����մϴ�.
print("Process Start")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# �ϳ��� ��ĥ ���ϵ��� ����� ���� �̸��� �ý������κ��� �Է¹޽��ϴ�..
directory = sys.argv[1]

# �ӽ÷� ������ ����� ������ �̸��� �����մϴ�.
temp_file_name = "temp.csv"

# ���� ����� ���� �̸��� �����մϴ�.
outfile_name = "merged_ID.xlsx"

# ����� ������ �����մϴ�. �� �� �ؽ�Ʈ������ �����˴ϴ�.
# ���ڵ��� utf-8�� ������ �Ϳ� �ָ��ϼ���.
temp_file = open(temp_file_name, 'w', encoding="utf-8")

# ������ ���빰�� ������ ����� �����մϴ�.
input_files = os.listdir(directory)

# ����� ���õ� ������ �����մϴ�. ����� ������ ����̶� �����ϸ� �˴ϴ�.
headers = []
outfile_has_header = False

# ������ ���빰�� �ϳ��ϳ� �ҷ��� ��ġ�� �۾��� �����մϴ�.
# input_files�� ����� ���� �̸��� �� ���� �ϳ��� �ҷ��ɴϴ�.
for filename in input_files:
    # ��Ȥ �ؽ�Ʈ ������ �ƴ� ������ �������� �� �ֽ��ϴ�. �̰� �ɷ����ϴ�.
    if ".txt" not in filename:
        continue

    # �ؽ�Ʈ ������ �´ٸ�, ������ �о�ɴϴ�.
    file = open(directory + "/" + filename)

    # ������ ���빰�� ������ ����Ʈ�� �����մϴ�.
    contents = []

    # ������ ���빰�� �� �پ� �о���鼭 �۾��� �����մϴ�.
    for line in file:
        # ���� ������ ��İ� ���빰�� �и��մϴ�.
        if ":" in line:
            splits = line.split(":")
            contents.append(splits[-1].strip())

            # ����� �����մϴ�. ���� 1ȸ�� ����˴ϴ�.
            if len(contents) > len(headers):
                headers.append(splits[0].strip())

    # ����� ���Ͽ� �Է��մϴ�. ���� 1ȸ�� ����˴ϴ�.
    if not outfile_has_header:
        header = ", ".join(headers)
        temp_file.write(header)
        outfile_has_header = True

    # ����� ���Ͽ� ���빰�� �Է��մϴ�.
    new_line = ", ".join(contents)
    temp_file.write("\n" + new_line)

    # �о�� ������ �����մϴ�.
    file.close()

# �ӽ� ����� ������ �����մϴ�.
temp_file.close()

# �ӽ÷� ����� ����� ������ �������·� ��ȯ�մϴ�.
PC.merge_all_to_a_book([temp_file_name], outfile_name)

# �ӽ÷� ����� ������� �����մϴ�.
os.remove(temp_file_name)

# �۾� ���� �޽����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")