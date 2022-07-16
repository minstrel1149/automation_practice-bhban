# 여기 있던 utf-8 관련 내용을 지우니까 syntax error가 없어짐.

from pathlib import Path
import time
import random
import os
# csv모듈을 활용하여 생성 시도
import csv

num_samples = 1000
alphabet_samples = 'abcdefghijklmnopqrstuvwxyz1234567890'

def random_string(length):
    result = ''
    for i in range(length):
        result += random.choice(alphabet_samples)
    return result

first_name_samples = '김이박최정강조윤장임'
middle_name_samples = '민서예지도하주윤채현지'
last_name_samples = '준윤우원호후서연아은진'

def random_name():
    result = ''
    result += random.choice(first_name_samples)
    result += random.choice(middle_name_samples)
    result += random.choice(last_name_samples)
    return result

try:
    (Path.cwd() / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 4] 컴퓨터! 엑셀 정리좀 해 놔, 10초 안에!' / '2_4_1_예제용 CSV 파일 1천 개, 1초만에 만들기' / 'personal_info_tkim1').mkdir()
except:
    print('이미 존재하는 폴더입니다.')

p1 = Path.cwd() / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 4] 컴퓨터! 엑셀 정리좀 해 놔, 10초 안에!' / '2_4_1_예제용 CSV 파일 1천 개, 1초만에 만들기' / 'personal_info_tkim1'

for i in range(num_samples):
    # 괄호가 꼭 있어야!
    name = random_name()
    filename = p1 / f'{i+1}_{name}.csv'
    # 'euc_kr'에 대한 decode 오류가 계속 생기는데.. 어떻게 해결?
    # 여기서 경로에러도 생기는 듯 한데.. 위 random_name에서 ()가 없어서 발생한 문제.
    outfile = open(filename, mode='w', newline='')
    header = ['이름', '나이', '메일', '전화', '성별']
    age = random.randint(20, 39)
    email = f'{random_string(8)}@taehwakim.co.kr'
    telephone = f'010-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}'
    sex = random.choice(['남성', '여성'])
    # csv모듈을 활용하기 위해 DictWriter 함수 사용
    output = csv.DictWriter(outfile, header)
    output.writeheader()
    output.writerow(dict(zip(header, [name, age, email, telephone, sex])))
    outfile.close()

print('Process Done!')
