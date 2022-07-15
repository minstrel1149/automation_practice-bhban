#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.02.15.
"""
import time
import os
from PIL import Image
import sys

# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ��Ǯ�� �̹��� �̸��� �Է¹޽��ϴ�.
image_filename = sys.argv[1]

# ������� ������ ������ �����մϴ�.
out_dir ="augmentation"
if out_dir not in os.listdir():
    os.mkdir(out_dir)

# ���� �̹��� ������ �ҷ��ɴϴ�.
image = Image.open(image_filename)
Xdim, Ydim = image.size

# ����� ���� ������ ������ �� ī���͸� �����մϴ�.
COUNT = 1

# �ϴ� ������ �����մϴ�. 2�� 0��
# ������ ������ �̸��� �Է��մϴ�.
temp_new_file_name = "%05d.png" %COUNT
# ī��Ʈ�� 1 ������ŵ�ϴ�.
COUNT += 1
# ���� �̹����� �����մϴ�.
image.save(out_dir + "/" + temp_new_file_name)
image.close()

# ��� ���ϸ��� ������ ����Ʈ�� ����ϴ�.
FILELIST = [temp_new_file_name]

# ���� ���� �̹����� ��� �о�� �¿��Ī�� �����մϴ�. 2�� 1��
for i in range(len(FILELIST)):
    # ������ �ҷ��ɴϴ�.
    image = Image.open(out_dir + "/" + FILELIST[i])
    # ��ȯ�� ������ �����ϱ� ���� ���ο� �̸��� �����մϴ�.
    new_temp_name = "%05d.png" %COUNT
    # ������ �� �� ������������� count�� 1�� ������ŵ�ϴ�.
    COUNT += 1
    # �̹����� �¿� �����մϴ�.
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    # �¿� ������ �̹����� �����մϴ�.
    image.save(out_dir + "/" + new_temp_name)
    image.close()
    # ��� ���ϸ��� ����Ʈ�� �����մϴ�.
    FILELIST.append(new_temp_name)

# ����Ʈ ���� �̹����� ��� �о�� ���ϴ�Ī�� �����մϴ�. 2�� 2��
for i in range(len(FILELIST)):
    # ������ �ҷ��ɴϴ�.
    image = Image.open(out_dir + "/" + FILELIST[i])
    # ��ȯ�� ������ �����ϱ� ���� ���ο� �̸��� �����մϴ�.
    new_temp_name = "%05d.png" % COUNT
    # ������ �� �� ������������� count�� 1�� ������ŵ�ϴ�.
    COUNT += 1
    # �̹����� ���� �����մϴ�.
    image = image.transpose(Image.FLIP_TOP_BOTTOM)
    # ���� ������ �̹����� �����մϴ�.
    image.save(out_dir + "/" + new_temp_name)
    image.close()
    # ��� ���ϸ��� ����Ʈ�� �����մϴ�.
    FILELIST.append(new_temp_name)

# ����Ʈ ���� �̹����� ��� �о�� �������� �����մϴ�. 2�� 3��
for i in range(len(FILELIST)):
    # ������ �ҷ��ɴϴ�.
    image = Image.open(out_dir + "/" + FILELIST[i])
    # ��ȯ�� ������ �����ϱ� ���� ���ο� �̸��� �����մϴ�.
    new_temp_name = "%05d.png" % COUNT
    # ������ �� �� ������������� count�� 1�� ������ŵ�ϴ�.
    COUNT += 1
    # �̹����� ������� ����ϴ�.
    image = image.convert('1')
    # ������� ��ȯ�� �̹����� �����մϴ�.
    image.save(out_dir + "/" + new_temp_name)
    image.close()
    # ��� ���ϸ��� ����Ʈ�� �����մϴ�.
    FILELIST.append(new_temp_name)

# ����Ʈ ���� �̹����� ��� �о�� 1���� ȸ���մϴ�. 2�� 3�� * 180
for el in FILELIST:
    for i in range(180):
        # ����ϰ� 1,000�常 ����ô�.
        # ������� 1000���� �Ѿ�� �ڵ带 �����մϴ�.
        if COUNT > 1000:
            break
        # ������ �ҷ��ɴϴ�.
        image = Image.open(out_dir + "/" + el)
        # ��ȯ�� ������ �����ϱ� ���� ���ο� �̸��� �����մϴ�.
        new_temp_name = "%05d.png" % COUNT
        # ������ �� �� ������������� count�� 1�� ������ŵ�ϴ�.
        COUNT += 1
        # ������ ȸ����ŵ�ϴ�.
        image = image.rotate(i+1)
        # ��Ȥ �̹��� ũ�Ⱑ ����ȴٴ� �̾߱Ⱑ �־� resize()�� �����մϴ�.
        image = image.resize((Xdim, Ydim))
        # ȸ�� �� �̹����� �����մϴ�.
        image.save(out_dir + "/" + new_temp_name)
        image.close()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
