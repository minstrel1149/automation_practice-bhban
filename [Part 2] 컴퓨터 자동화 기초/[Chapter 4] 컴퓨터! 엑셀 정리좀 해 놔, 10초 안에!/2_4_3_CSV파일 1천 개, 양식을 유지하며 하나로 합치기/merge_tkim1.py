from pathlib import Path
import time
import random
import shutil
import os
# csv모듈을 활용하여 생성 시도 -> 책과는 관계 없이 내가 생각하는 방향으로
import csv

# 폴더를 복사하는 것부티 진행 -> shutil모듈 활용(copytree)
p1 = Path.cwd() / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 4] 컴퓨터! 엑셀 정리좀 해 놔, 10초 안에!' / '2_4_1_예제용 CSV 파일 1천 개, 1초만에 만들기' / 'personal_info_tkim1'
p2 = Path.cwd() / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 4] 컴퓨터! 엑셀 정리좀 해 놔, 10초 안에!' / '2_4_3_CSV파일 1천 개, 양식을 유지하며 하나로 합치기' / 'personal_info_tkim1'
p3 = Path.cwd() / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 4] 컴퓨터! 엑셀 정리좀 해 놔, 10초 안에!' / '2_4_3_CSV파일 1천 개, 양식을 유지하며 하나로 합치기'
try:
    shutil.copytree(p1, p2)
except:
    print('이미 존재하는 폴더입니다.')

files = os.listdir(p2)
outfile_name = 'merged_ID_tkim1.csv'

with open(p3 / outfile_name, mode='w', newline='') as write_file:
    # 헤더를 유지해야하므로 빈 헤더 일단 삽입
    header = []
    for filename in files:
        read_files = open(p2 / filename, mode='r')
        csv_reader = csv.reader(read_files)
        data = list(csv_reader)
        csv_writer = csv.writer(write_file)
        # 헤더가 비었으면 헤더를 추가하고 writerow로 csv에 헤더 삽입. 헤더가 비지 않았으면 별도 행동 미수행
        if len(data[0]) > len(header):
            header = data[0]
            csv_writer.writerow(header)
        # 여기서 원래 파일대로라면 csv_writer.writerow(data[1])로 기재하면 되지만, 여러 줄이 있을 경우를 대비 -> 범용성 고려
        for i in range(1, len(data)):
            csv_writer.writerow(data[i])

print('Process Done!')