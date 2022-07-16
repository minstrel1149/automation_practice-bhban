#-*-coding:euc-kr

import random
import time
import os
from pathlib import Path

print('Process Start.')
start_time = time.time()
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

# os.makedirs 대신 활용 가능. os.mkdir('')보다는 이게 원하는 경로에 폴더 생성할 수 있어서 좋은듯, try/except로 예외 처ㅣㄹ
try:
    (Path.cwd() / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 3] 컴퓨터! 커피 한 잔 마시고 올게, 전부 정리해놔!' / '2_3_1_회원 개인정보 파일 1천 개, 1초만에 만들기' / 'personal_info_tkim1').mkdir()
except:
    print('이미 존재하는 폴더입니다.')
p = Path.cwd() / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 3] 컴퓨터! 커피 한 잔 마시고 올게, 전부 정리해놔!' / '2_3_1_회원 개인정보 파일 1천 개, 1초만에 만들기' / 'personal_info_tkim1'

# 0번 대신 1번부터 시작하도록 바꾸고 f-string 이용
for i in range(num_samples):
    name = random_name()
    filename = p / f'{i+1}_{name}.txt'
    # open으로 열고 닫는 대신 with as 구문으로 처리
    with open(filename, mode='w') as outfile:
        outfile.write(f'이름: {name}\n')
        # time.time에서 뒷 자리를 이용하는 것보다 random.randint로 나이대 한정
        outfile.write(f'나이: {random.randint(20, 39)}\n')
        outfile.write(f'메일: {random_string(8)}@taehwakim.co.kr\n')
        # 마찬가지로 random.randint 사용
        outfile.write(f'전화: 010-{random.randint(1111, 9999)}-{random.randint(1111, 9999)}\n')
        outfile.write(f'성별: {random.choice(["남성", "여성"])}\n')

print('Process Done!')

end_time = time.time()

print(f'{start_time - end_time} seconds.')
