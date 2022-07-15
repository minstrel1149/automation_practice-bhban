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
from PIL import ImageFont
from PIL import ImageDraw
import sys

# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ��� ��������� ����� ������ �ý������κ��� �Է¹޽��ϴ�.
member_photo = sys.argv[1]

# ���������� ����� CSV������ �ҷ��ɴϴ�.
personal_IDs = sys.argv[2]

# ���Կ� ������ �ΰ� ������ �Է¹޽��ϴ�.
logo_filename = sys.argv[3]

# ���Կ� ������ ���ø� ������ �Է¹޽��ϴ�.
template_filename = sys.argv[4]

try:
    template = Image.open(template_filename)
except:
    template = Image.new("RGBA", (800, 1268), 'white')

Xdim, Ydim = template.size

# ������� ������ ȸ�� ������ �����մϴ�.
url = "https://bit.ly/2FqKtba"

# ������� ������ ������ �����մϴ�.
out_dir ="idcards"
if out_dir not in os.listdir():
    os.mkdir(out_dir)

# �ΰ� ������ �ҷ��ɴϴ�.
logo = Image.open(logo_filename)
logo_x, logo_y = logo.size

# ������� ����� �ҷ��ɴϴ�.
photos = os.listdir(member_photo)
PHOTOS = []
for el in photos:
    if el.strip().split(".")[-1] not in "PNG png JPG jpg BMP bmp JPEG jpeg":
        continue
    PHOTOS.append(el)

# ���ݱ��� ������ ���� ������ �����ϴ� ī���͸� ����ϴ�.
COUNT = 0

# �ΰ� ũ�⸦ �����ϱ� ���� �����մϴ�. ������� ���ΰ� ª���� ���� ���̸� �������� �۾��մϴ�.
# �ΰ��� �ʺ� ����� �ʺ��� 20%�� �����մϴ�.
new_logo_x = int(Xdim * 0.2)
# �ΰ��� y�� ���̴� ��ʽ����� ����մϴ�.
# new_logo_y : logo_y = new_logo_x : logo_x
# �����մϴ�. �ʵ��б��� �ٵ� ������ϴ�.
new_logo_y = int(logo_y * (new_logo_x / logo_x))

# ������� �����ϱ� ���� �ΰ� ũ�⸦ �����մϴ�.
resized_logo = logo.resize((new_logo_x, new_logo_y))

# ���� �� �ΰ� �ݾ��ݴϴ�.
logo.close()

# ���������� �ҷ��ɴϴ�.
IDs = open(personal_IDs)

# ����� �̾Ƴ��ϴ�.
header = IDs.readline()

# �� ����� ���ϴܿ� �ΰ� �����ϰڽ��ϴ�.
# ���� ������ 10%, 5%���� �ָ� �����ϰ���? �̰� �������� ���⿡ �޷� �ֽ��ϴ�.
template.paste(resized_logo, (int(Xdim * 0.1), int(Ydim * 0.95 - new_logo_y)))

# �ΰ� �ݾ��ݴϴ�.
resized_logo.close()

# ������� ������ ��Ʈ���� �����մϴ�.
# ��Ʈ �̸��� �����Ͻø� �ٲ�ϴ�. �⺻�� �����Դϴ�. ��ǻ�͸� �� ������ �����Դϴ�.
# �̸��� ū ���ڷ� �����սô�.
nameFont = ImageFont.truetype("font/gulim.ttc", 70)
# URL�� �ּҴ� ������ �۰� �����Ұ̴ϴ�.
smallFont = ImageFont.truetype("font/gulim.ttc", 40)
# ������ �������� ������ ũ��� �ۼ��մϴ�.
infoFont = ImageFont.truetype("font/gulim.ttc", 50)

# ����� ���� �ֻ�ܿ� URL�� �����մϴ�.
# �¿� ������ �� ���� 5%�� ���̴ϴ�.
x_offset = int(Xdim * 0.95 - smallFont.getsize(url)[0])
# ��� ������ 2%������ ����� �� �����ϴ�.
y_offset = int(Ydim * 0.02)
# ������� Ȩ������ �ּҸ� �����մϴ�.
ImageDraw.Draw(template).text(xy=(x_offset, y_offset), text=url, font=smallFont, fill="black")

# ���������� ���پ� �о���鼭, �� ���� ������� �� �徿 ����̴ϴ�.
for line in IDs:
    # CSV�ϱ� �ĸ� ������ �ɰ� �� �ֽ��ϴ�. �ɰ��ô�.
    splt = line.strip().split(", ")

    # ������� �� �����鸸 �����մϴ�.
    name = splt[0]
    division = splt[3]

    # ����� ���ø��� �����մϴ�.
    idcard = template.copy()

    # ������ ������ �ҷ��ɽô�.
    photo_for_id = Image.open(member_photo + "/" + PHOTOS[COUNT])

    # ������ �ʺ� ����� �ʺ��� 50% ũ��� �����մϴ�.
    photo_for_id = photo_for_id.resize((int(Xdim/2), int(Xdim/2 * (4/3))))

    # ������ ����� �� �߾ӿ� �����սô�.
    idcard.paste(photo_for_id, (int(Xdim/4), int(Ydim/2 - Xdim/2*(4/3)/2)))

    # �̸��� �����Ұ̴ϴ�.
    # �̸� ���̻��� ������ �����ؼ� �� �� ���̰� �մϴ�.
    temp_name = ""
    for el in name:
        temp_name += el + " "
    name = temp_name[:-1]

    # �̸��� �¿� ��������Ұ̴ϴ�.
    x_offset = int(Xdim * 0.5 - nameFont.getsize(name)[0]/2)
    # ���� ������ 20%�� �ݽô�.
    y_offset = int(Ydim * 0.8 - nameFont.getsize(name)[1])
    # ���Կ� �̸��� �����մϴ�.
    ImageDraw.Draw(idcard).text(xy=(x_offset, y_offset), text=name, font=nameFont, fill="black")

    # �̸� �ؿ� �μ����� �����Ұ̴ϴ�.
    # �μ��� ��������Դϴ�.
    x_offset = int(Xdim * 0.5 - infoFont.getsize(division)[0]/2)
    # ���� ������ 15%�� �ݽô�.
    y_offset = int(Ydim * 0.85 - infoFont.getsize(division)[1])
    # ���Կ� �̸��� �����մϴ�.
    ImageDraw.Draw(idcard).text(xy=(x_offset, y_offset), text=division, font=infoFont, fill="black")

    # �ϼ��� ������� �����մϴ�.
    idcard.save(out_dir + "/" + PHOTOS[COUNT])

    # ���嵵 ������ ������ �ݾ��ݴϴ�.
    idcard.close()

    COUNT += 1

# ���ø��� �ݾ��ݴϴ�.
template.close()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
