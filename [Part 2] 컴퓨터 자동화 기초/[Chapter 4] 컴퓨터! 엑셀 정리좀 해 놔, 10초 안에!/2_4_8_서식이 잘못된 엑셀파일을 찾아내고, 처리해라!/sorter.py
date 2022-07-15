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

# ���� ���÷� ����� ���� �̸��� �ý������κ��� �Է¹޽��ϴ�.
template = sys.argv[1]

# ���ϵ��� ����� ���� �̸��� �ý������κ��� �Է¹޽��ϴ�.
directory = sys.argv[2]

# �۵� ��带 �ý������κ��� �Է¹޽��ϴ�.
MODE = sys.argv[3]

# ������ ���빰�� ������ ����� �����մϴ�.
input_files = os.listdir(directory)

# ���ø� ������ �о�� ����� �и��մϴ�.
HEADER = px.get_array(file_name=template)[0]

# ���� ����� ��� �� ��� ������ �����Ǿ����� ���� ���� ī���͸� ����ϴ�.
if MODE in "DELETEdelete":
    count = 0
# ���� ����� ��� ���� �ۼ��� ���� ������ �����մϴ�.
elif MODE in "REPORTreport":
    REPORT = open("report.txt", 'w')
# �з� ����� ��� �з��� ������ �����ϱ� ���� ������ �����մϴ�.
elif MODE in "SEPARATEseparate":
    os.mkdir("wrong_files")
    # ���� �̵��� �����ϱ� ���� ���̺귯���� �ҷ��ɴϴ�.
    import shutil

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
    if HEADER == header:
        # ��ġ�Ѵٸ� ����ӽô�.
        continue

    # ��ġ���� �ʴ´ٸ� �� �Ʒ� �κ��� �ڵ尡 �۵��˴ϴ�.
    if MODE in "DELETEdelete":
        # ���� ����� ��� �����մϴ�.
        os.remove(directory + "/" + filename)
        count += 1
    elif MODE in "REPORTreport":
        # ���� ����� ��� ������ ���� �̸��� �����մϴ�.
        REPORT.write(filename + "\n")
    elif MODE in "SEPARATEseparate":
        # �з� ����� ��� ������ ������ ������ �̵���ŵ�ϴ�.
        shutil.move(directory + "/" + filename, "wrong_files/" + filename)

# ���� ����� ��� �� ��� ������ �����Ǿ����� ����մϴ�.
if MODE in "DELETEdelete":
    print("Total " + str(count) + " files were removed.")

# ���� ����� ��� ������ �����մϴ�.
if MODE in "REPORTreport":
    REPORT.close()

# �۾� ���� �޽����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
