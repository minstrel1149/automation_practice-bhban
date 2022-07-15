#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.02.17.
"""
import time
import os
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import sys
import datetime

# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ��������ڰ� ����� CSV������ �ҷ��ɴϴ�.
personal_IDs = sys.argv[1]

# ��� ���ø� ������ �Է¹޽��ϴ�.
template_filename = sys.argv[2]

# ���ø��� �����ݴϴ�.
template = Image.open(template_filename)
Xdim, Ydim = template.size


# ������� ������ ������ �����մϴ�.
out_dir ="suryojungs"
if out_dir not in os.listdir():
    os.mkdir(out_dir)

# ���������� �ҷ��ɴϴ�.
IDs = open(personal_IDs)

# ����� �̾Ƴ��ϴ�.
header = IDs.readline()

# ������(����)�� ������ ��Ʈ���� �����մϴ�.
# ��Ʈ �̸��� �����Ͻø� �ٲ�ϴ�. �⺻�� �����Դϴ�. ��ǻ�͸� �� ������ �����Դϴ�.
# �̸��� ū ���ڷ� �����սô�.
nameFont = ImageFont.truetype("font/gulim.ttc", 30)
# ������¥�� ���� �� ���� ��Ʈ�� �����սô�.
dateFont = ImageFont.truetype("font/gulim.ttc", 25)
# ������ȣ�� �� �� ���� ��Ʈ�� �����սô�.
smallFont = ImageFont.truetype("font/gulim.ttc", 18)

# ��濡 �Է��� �������ڸ� ����մϴ�.
date = str(datetime.datetime.today().date())
date = date.split("-")
DATE = date[0] + "�� " + date[1] + "�� " + date[2] + "��"

# ������¥�� ��濡 �Է��մϴ�.
# �¿� ������ ��������Դϴ�.
x_offset = int(Xdim / 2 - dateFont.getsize(DATE)[0]/2)
# ���� ������ ���� 30% ���� ��ƺ��ϴ�.
y_offset = int(Ydim * .7)
# ��濡 ������¥�� �����մϴ�.
ImageDraw.Draw(template).text(xy=(x_offset, y_offset), text=DATE, font=dateFont, fill="black")

# ���ݱ��� ������ ���� ������ �����ϴ� ī���͸� ����ϴ�.
# �������� ���۹�ȣ�� �����ֽø� �˴ϴ�. ������� ������ 50������ �����ϸ� COUNT=50�Դϴ�.
COUNT = 0

# ���������� ���پ� �о���鼭, �� ���� ������(����)�� �� �徿 ����̴ϴ�.
for line in IDs:
    # CSV�ϱ� �ĸ� ������ �ɰ� �� �ֽ��ϴ�. �ɰ��ô�.
    splt = line.strip().split(", ")

    # �̸��� �ҼӸ� �����մϴ�.
    name = splt[0]
    division = splt[3]

    # ������(����) ���ø��� �����մϴ�.
    suryojung = template.copy()

    # �̸��� �����Ұ̴ϴ�.
    # �̸� ���̻��� ������ �����ؼ� �� �� ���̰� �մϴ�.
    temp_name = ""
    for el in name:
        temp_name += el + " "
    # �̸��� ������(����)�� �����ϱ� ���� ������� �ٵ���ݴϴ�.
    name = "��      �� : " + temp_name[:-1]

    # �μ����� �����Ұ̴ϴ�.
    # �μ��� ���̻��� ������ �����ؼ� �� �� ���̰� �մϴ�.
    temp_division = ""
    for el in division:
        temp_division += el + " "
    # �μ����� ������(����)�� �����ϱ� ���� ������� �ٵ���ݴϴ�.
    division = "�ҼӺμ� : " + temp_division

    # �̸��� ���� �������κ��� 15% ������ ���� �����սô�.
    x_offset = int(Xdim * 0.15)
    # �̸��� ���� ������κ��� 35% ��ġ�� �����սô�.
    y_offset = int(Ydim * 0.35)
    # ������(����)�� �̸��� �����մϴ�.
    ImageDraw.Draw(suryojung).text(xy=(x_offset, y_offset), text=name, font=nameFont, fill="black")

    # �μ����� �̸����� �� �� �Ʒ��� �����ؾ߰���.
    y_offset += nameFont.getsize(name)[1]*1.5
    # ������(����)�� �μ����� �����մϴ�.
    ImageDraw.Draw(suryojung).text(xy=(x_offset, y_offset), text=division, font=nameFont, fill="black")

    # ������ȣ�� �Է��ؾ߰���?
    suyeo = "������ȣ : %d-%06d" % (int(DATE[:4]),  COUNT)
    # ������ȣ�� �� 12%�����뿡 �Է��սô�.
    y_offset = int(Ydim * 0.12)
    # ������(����)�� ������ȣ�� �����մϴ�.
    ImageDraw.Draw(suryojung).text(xy=(x_offset, y_offset), text=suyeo, font=smallFont, fill="black")

    # �ϼ��� ������ �����մϴ�.
    suryojung.save(out_dir + "/" + str(COUNT) + ".png")

    # ���嵵 ������ �̹����� �ݾ��ݴϴ�.
    suryojung.close()

    COUNT += 1

# ���ø��� �ݾ��ݴϴ�.
template.close()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
