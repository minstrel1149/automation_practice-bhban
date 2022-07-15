#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.02.12.
"""
import time
import os
import sys

# �۾� ���� �޽����� ����մϴ�.
print("Process Start")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# �ϳ��� ��ĥ ���ϵ��� ����� ���� �̸��� �ý������κ��� �Է¹޽��ϴ�.
directory = sys.argv[1]

# ����� ������ �̸��� �����մϴ�.
outfile_name = "merged_ID.csv"

# ����� ������ �����մϴ�. �� �� �ؽ�Ʈ������ �����˴ϴ�.
out_file = open(outfile_name, 'w')

# ������ ���빰�� ������ ����� �����մϴ�.
input_files = os.listdir(directory)

# ����� ���õ� �Ҹ��� ������ �����մϴ�. ����� ������ ����̶� �����ϸ� �˴ϴ�.
outfile_has_header = False

# ������ ���빰�� �ϳ��ϳ� �ҷ��� ��ġ�� �۾��� �����մϴ�.
# input_files�� ����� ���� �̸��� �� ���� �ϳ��� �ҷ��ɴϴ�.
for filename in input_files:
    # ��Ȥ csv ������ �ƴ� ������ �������� �� �ֽ��ϴ�. �̰� �ɷ����ϴ�.
    if ".csv" not in filename:
        continue

    # csv ������ �´ٸ�, ������ �о�ɴϴ�.
    file = open(directory + "/" + filename)

    # ����� �и��մϴ�.
    header = file.readline()

    # ����� ���Ͽ� �Է��մϴ�. ���� 1ȸ�� ����˴ϴ�.
    if not outfile_has_header:
        out_file.write(header.strip())
        outfile_has_header = True

    # ����� ���Ͽ� ���빰�� �Է��մϴ�.
    out_file.write("\n" + file.read())

    # �о�� ������ �����մϴ�.
    file.close()

# ����� ������ �����մϴ�.
out_file.close()

# �۾� ���� �޽����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
