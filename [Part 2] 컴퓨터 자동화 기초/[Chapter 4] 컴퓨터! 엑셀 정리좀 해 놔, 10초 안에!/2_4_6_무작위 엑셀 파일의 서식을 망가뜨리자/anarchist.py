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
import random

# �۾� ���� �޽����� ����մϴ�.
print("Process Start")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ������ �����߸� ���ϵ��� ����� ���� �̸��� �ý������κ��� �Է¹޽��ϴ�.
directory = sys.argv[1]

# �� �ۼ�Ʈ�� �Ǵ� ������ ������ �����߸��� ������ �ý������κ��� �Է¹޽��ϴ�.
percent = float(sys.argv[2]) / 100

# ������ ���빰�� ������ ����� �����մϴ�.
input_files = os.listdir(directory)

# ������ �����߸� �� ���� ������ ����մϴ�.
DESTROY_COUNT = int(len(input_files) * percent)

# ���� ������ ��������ϴ�.
random.shuffle(input_files)

# �ı� ����� �� �ҽ��� ���� ����� ����ϴ�.
destroy_them = input_files[:DESTROY_COUNT]

# �� 3���� ����� �غ��߽��ϴ�. ����� ����Ű�� ���� ī��Ʈ�� ���մϴ�.
# ī��Ʈ�ٿ��� �ϴٰ� shift_1, shift_2�� �Ǹ� ����� ������ �ٲ�ϴ�.
shift_1 = DESTROY_COUNT/3*2
shift_2 = DESTROY_COUNT/3

# ������ �ı��� ���ϵ��� �ϳ��� �о�� �۾��� �����մϴ�.
# destroy_them�� ����� ���� �̸��� �� ���� �ϳ��� �ҷ��ɴϴ�.
for filename in destroy_them:
    # ��Ȥ xlsx ������ �ƴ� ������ �������� �� �ֽ��ϴ�. �̰� �ɷ����ϴ�.
    if ".xlsx" not in filename:
        continue

    # ���� ������ �´ٸ�, ������ �о�ɴϴ�.
    file = px.get_sheet(file_name=directory + "/" + filename)

    # ���� �ִ� ������ ���������ô�. ������ ���� ���ϴ�.
    os.remove(directory + "/" + filename)

    # ���� ������ ����Ʈ�� ��ȯ�մϴ�.
    data_array = file.array

    # column ������ �����߸��°� ���� �����ϴ�. column�� ����� �˾Ƴ��ô�.
    num_columns = len(data_array[0])
    # ������ ���� �ϳ� �����߸��� ���� ���� ���ڸ� �����մϴ�.
    victim = random.randint(0, num_columns - 1)

    # ù ��° ����Դϴ�.
    if DESTROY_COUNT > shift_1:
        # ������ ���� �ϳ� ���������ϴ�.
        file.delete_columns([victim])

    # �� ��° ����Դϴ�.
    elif DESTROY_COUNT > shift_2:
        # ���õ� ���� ������ �ٿ��־� �����ϴ�.
        file.column += file.column[victim].copy()

    # �� ��° ����Դϴ�.
    else:
        # �ٲ�ġ���� ���� ����ϴ�. ���빰�� ��� '�����'�� ä�������ϴ�. �߿�.
        CAT = ["�����" for i in range(file.number_of_rows())]

        # ���� ���� ������ ���빰�� ����̸� �ٲ�ġ���մϴ�. �߿�.
        file.column[victim] = CAT

    # ������ ������ �ҽ��� ���������� �����մϴ�.
    px.save_as(array=data_array, dest_file_name=directory + "/" + filename)

    # ī��Ʈ�ٿ��� �� ���� �մϴ�.
    DESTROY_COUNT -= 1

# �۾� ���� �޽����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
