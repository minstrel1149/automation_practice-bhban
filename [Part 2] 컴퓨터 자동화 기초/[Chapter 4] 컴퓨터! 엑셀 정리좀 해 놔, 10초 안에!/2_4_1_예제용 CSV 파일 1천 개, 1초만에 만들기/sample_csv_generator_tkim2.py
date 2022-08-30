from pathlib import Path
import os
import random
import csv
import string

num_samples = 1000
alphabet_samples = string.ascii_lowercase + string.digits

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
    (Path.home() / 'bhban_rpa-master' / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 4] 컴퓨터! 엑셀 정리좀 해 놔, 10초 안에!' / '2_4_1_예제용 CSV 파일 1천 개, 1초만에 만들기' / 'personal_info_tkim2').mkdir()
except:
    print('이미 존재하는 폴더입니다.')

p = Path.home() / 'bhban_rpa-master' / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 4] 컴퓨터! 엑셀 정리좀 해 놔, 10초 안에!' / '2_4_1_예제용 CSV 파일 1천 개, 1초만에 만들기' / 'personal_info_tkim2'

# csv모듈을 활용할 경우 : 아래와 같은 코드 활용 가능
# outfile = open(filename, mode='w', newline='')
# output = csv.DictWriter(outfile, header)
# output.writeheader()
# output.writerow(dict(zip(header, [name, age, email, telephone, sex])))
# outfile.close()

for i in range(num_samples):
    name = random_name()
    header = ['이름', '나이', '메일', '전화', '성별']
    age = random.randint(20, 39)
    email = f'{random_string(random.randint(5, 9))}@taehwakim.co.kr'
    phone = f'010-{random.randint(1111, 9999)}-{random.randint(1111, 9999)}'
    sex = random.choice(['남성', '여성'])
    # csv 파일 생성을 위해서는 open() 시 newline=''를 넣어줘야 불필요한 엔터 공백 제거 가능
    with open(p / f'{i+1}_{name}.csv', mode='w', newline='') as write_file:
        write_file.write(', '.join(header) + '\n')
        write_file.write(f'{name}, {age}, {email}, {phone}, {sex}\n')

print('Process Done!')
