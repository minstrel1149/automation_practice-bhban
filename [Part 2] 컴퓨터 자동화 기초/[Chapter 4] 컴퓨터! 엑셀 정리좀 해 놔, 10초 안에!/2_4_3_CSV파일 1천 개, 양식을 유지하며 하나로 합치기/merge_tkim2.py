from email import header
from pathlib import Path
import time
import random
import shutil
import os
# csv모듈을 활용하여 생성 시도 -> 책과는 관계 없이 내가 생각하는 방향으로
import csv

p1 = Path.home() / 'bhban_rpa-master' / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 4] 컴퓨터! 엑셀 정리좀 해 놔, 10초 안에!' / '2_4_1_예제용 CSV 파일 1천 개, 1초만에 만들기' / 'personal_info_tkim2'
p2 = Path.home() / 'bhban_rpa-master' / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 4] 컴퓨터! 엑셀 정리좀 해 놔, 10초 안에!' / '2_4_3_CSV파일 1천 개, 양식을 유지하며 하나로 합치기' / 'personal_info_tkim2'
p3 = Path.home() / 'bhban_rpa-master' / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 4] 컴퓨터! 엑셀 정리좀 해 놔, 10초 안에!' / '2_4_3_CSV파일 1천 개, 양식을 유지하며 하나로 합치기'
try:
    shutil.copytree(p1, p2)
except:
    print('이미 존재하는 폴더입니다.')

files = [x.name for x in p2.glob('*.csv')]

with open(p3 / 'merged_ID_tkim2.csv', mode='w', newline='') as write_file:
    csv_writefile = csv.writer(write_file)
    header = []
    for filename in files:
        read_file = open(p2 / filename, mode='r')
        csv_readfile = csv.reader(read_file)
        data = list(csv_readfile)
        if header == []:
            header = data[0]
            csv_writefile.writerow(header)
        for i in range(1, len(data)):
            csv_writefile.writerow(data[i])

print('Process Done!')