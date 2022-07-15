#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.02.13.
"""
import time
import os
from PIL import Image
import sys

# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ������ ����� �������� �Է¹޽��ϴ�.
directory = sys.argv[1]

# �� �ۼ�Ʈ ������ ����� ������ ������ �Է¹޽��ϴ�.
percent = float(sys.argv[2])/100

# ������� ������ ������ �����մϴ�.
out_dir ="resized_image"
if out_dir not in os.listdir():
    os.mkdir(out_dir)


# ������ ���빰�� ������ ����� �����մϴ�.
input_files = os.listdir(directory)

# input_files�� ����� ���� �̸��� �� ���� �ϳ��� �ҷ��ɴϴ�.
for filename in input_files:
    # ��Ȥ �̹��� ������ �ƴ� ������ �������� �� �ֽ��ϴ�. �̰� �ɷ����ϴ�.
    exp = filename.strip().split('.')[-1]
    if exp not in "JPG jpg JPEG jpeg PNG png BMP bmp":
        continue

    # �̹����� �ҷ��ɴϴ�.
    image = Image.open(directory + "/" + filename)

    # �̹����� ũ�⸦ �˾Ƴ��ϴ�.
    Xdim, Ydim = image.size

    # ���⿡ ������ ���� ���ο� �̹����� ����� ����մϴ�.
    Xdim *= percent
    Ydim *= percent

    # �̹��� ����� �����մϴ�.
    image = image.resize((int(Xdim), int(Ydim)))

    # ����� �̹����� �����մϴ�.
    image.save(out_dir + "/" + filename)

    # �̹����� �ݾ��ݴϴ�.
    image.close()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
