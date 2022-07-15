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

# ������ ������ �ΰ� ������ �Է¹޽��ϴ�.
logo_filename = sys.argv[2]

# ������� ������ ������ �����մϴ�.
out_dir ="images_with_logo"
if out_dir not in os.listdir():
    os.mkdir(out_dir)


# ������ ���빰�� ������ ����� �����մϴ�.
input_files = os.listdir(directory)

# �ΰ� ������ �ҷ��ɴϴ�.
logo = Image.open(logo_filename)
logo_x, logo_y = logo.size

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

    # �ΰ������� �̹����� �°� ������ Ȯ��/����մϴ�.
    # �̹����� �ΰ��� ����/���� ������ �ٸ��� ������ ��ʽ��� ����ؾ� �մϴ�.
    # �ʵ��б� ���������Դϴ�. ���� ����� ���δٸ� �����Դϴ�. �ƹ�ư ����̴ϴ�.

    # �� ��� �ΰ��� X�� ���̰� �̹����� ���ؼ� �� ��ϴ�.
    if logo_x / Xdim > logo_y / Ydim:
        # �ΰ��� x�� ���̸� �̹����� x�� ������ 1/5�� �����մϴ�.
        new_logo_x = int(Xdim/5)
        # �ΰ��� y�� ���̴� ��ʽ����� ����մϴ�.
        # new_logo_y : logo_y = new_logo_x : logo_x
        # �����մϴ�. �ʵ��б��� �ٵ� ������ϴ�.
        new_logo_y = int(logo_y * (new_logo_x / logo_x))
    # �ΰ��� y�� ���̰� �̹����� ���� �� ��� �ݴ�� �մϴ�.
    else:
        new_logo_y = int(Ydim / 5)
        new_logo_x = int(logo_x * (new_logo_y / logo_y))

    # �̹��� ũ�⿡ �°� ���/Ȯ��� �ΰ��Դϴ�.
    resized_logo = logo.resize((new_logo_x, new_logo_y))

    # �Է¹��� ������ �ΰ� �����մϴ�. ������ ��ġ�� ������.
    # ���� ������ 2%���� �ָ� �����ϰ���? �̰� �������� ���⿡ �޷� �ֽ��ϴ�.
    image.paste(resized_logo, (int(Xdim/50), int(Ydim/50)), resized_logo)

    # ����� �̹����� �����մϴ�.
    image.save(out_dir + "/" + filename)

    # �̹����� �ݾ� �ݴϴ�.
    image.close()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
