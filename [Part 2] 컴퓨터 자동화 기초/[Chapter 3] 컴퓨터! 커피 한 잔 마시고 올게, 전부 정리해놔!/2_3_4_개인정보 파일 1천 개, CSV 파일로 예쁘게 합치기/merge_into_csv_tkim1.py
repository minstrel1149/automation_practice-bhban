#-*-coding:utf-8

from pathlib import Path
import os
import shutil
# 다음에는 csv 모듈을 사용해보는 것으로
import csv

# 폴더를 복사하는 것부티 진행 -> shutil모듈 활용(copytree)
p1 = Path.cwd() / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 3] 컴퓨터! 커피 한 잔 마시고 올게, 전부 정리해놔!' / '2_3_3_회원 개인정보 파일 1천 개, CSV 파일 하나로 합치기' / 'personal_info_tkim1'
p2 = Path.cwd() / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 3] 컴퓨터! 커피 한 잔 마시고 올게, 전부 정리해놔!' / '2_3_4_개인정보 파일 1천 개, CSV 파일로 예쁘게 합치기' / 'personal_info_tkim1'
p3 = Path.cwd() / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 3] 컴퓨터! 커피 한 잔 마시고 올게, 전부 정리해놔!' / '2_3_4_개인정보 파일 1천 개, CSV 파일로 예쁘게 합치기'
try:
    shutil.copytree(p1, p2)
except:
    print('이미 존재하는 폴더입니다.')

outfile_name = 'merged_ID_tkim1.csv'

files = os.listdir(p2)

# with as구문으로 write_file open 진행
with open(p3 / outfile_name, mode='w') as write_file:
    # headers 빈 리스트 생성
    headers = []
    # 아직 write_file에 header가 없는 상태
    outfile_has_header = False
    for filename in files:
        if '.txt' not in filename:
            continue
        read_file = open(p2 / filename, mode='r')
        # contents를 담을 빈 리스트 생성
        contents = []
        # readlines 메서드로 한 줄씩 반복
        for line in read_file.readlines():
            splits = line.split(':')
            contents.append(splits[-1].strip())
            # headers는 단 한번만 생성(빈 리스트에 추가하고 나면 contents와 header의 길이가 같아짐)
            if len(contents) > len(headers):
                headers.append(splits[0].strip())
        # if not outfile_has_header == if True (처음에는) -> 바꾸고 나면 if False가 됨
        if not outfile_has_header:
            header = ', '.join(headers)
            write_file.write(header)
            outfile_has_header = True
        new_line = ', '.join(contents)
        write_file.write(f'\n{new_line}')

print('Process Done!')