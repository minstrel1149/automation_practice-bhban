#-*-coding:euc-kr
"""
Author : Byunghyun Ban
GitHub : https://github.com/needleworm
Book : 6���� ġ ������ �Ϸ� ���� ������ ���� �ڵ�ȭ
Last Modification : 2020.02.13.
"""
import time
import os
import numpy as np
from PIL import Image


# �۾� ���� �޽����� ����մϴ�.
print("Process Start.")

# ���� ������ �ð��� ����մϴ�.
start_time = time.time()

# ������ �̹��� ���� ������ �����մϴ�.
NUM_SAMPLES = 1000

# ������� ������ ������ �����մϴ�.
out_dir ="random_image"
if out_dir not in os.listdir():
    os.mkdir(out_dir)


# NUM_SAMPLES ȸ����ŭ �ݺ��ϸ� �׸��� �����մϴ�.
# �̸��׸�, NUM_SAMPLES�� 100�̸� ���� �̹��� 100���� �����մϴ�.
for i in range(NUM_SAMPLES):
    # ������ ���� �̸��� ���մϴ�. ���� �ð��� �״�� ��������.
    name = str(time.time())[-7:] + ".png"

    # ���� �̹����� �����ϱ� ���� ����� �����մϴ�. ��������� �����Դϴ�.
    Xdim, Ydim = np.random.randint(100, 400, size=2)

    # ���� �̹����� �����մϴ�.
    image = np.random.randint(256, size=(Xdim, Ydim, 3)).astype('uint8')

    # ������� PIL Image ���·� ����ϴ�.
    result = Image.fromarray(image)

    # ����� ������ �����մϴ�.
    result.save(out_dir + "/" +name)

    # �̹����� �ݾ��ݴϴ�.
    result.close()

# �۾� ���� �޼����� ����մϴ�.
print("Process Done.")

# �۾��� �� �� �ʰ� �ɷȴ��� ����մϴ�.
end_time = time.time()
print("The Job Took " + str(end_time - start_time) + " seconds.")
