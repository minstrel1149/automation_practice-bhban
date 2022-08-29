from pathlib import Path
import os
import shutil
import csv

p1 = Path.home() / 'bhban_rpa-master' / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 3] 컴퓨터! 커피 한 잔 마시고 올게, 전부 정리해놔!' / '2_3_2_회원 개인정보 파일 1천 개, 텍스트 파일 하나로 합치기' / 'personal_info_tkim2'
p2 = Path.home() / 'bhban_rpa-master' / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 3] 컴퓨터! 커피 한 잔 마시고 올게, 전부 정리해놔!' / '2_3_4_개인정보 파일 1천 개, CSV 파일로 예쁘게 합치기' / 'personal_info_tkim2'
p3 = Path.home() / 'bhban_rpa-master' / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 3] 컴퓨터! 커피 한 잔 마시고 올게, 전부 정리해놔!' / '2_3_4_개인정보 파일 1천 개, CSV 파일로 예쁘게 합치기'
try:
    shutil.copytree(p1, p2)
except:
    print('이미 존재하는 폴더입니다.')

files = os.listdir(p2)

outfile_name = 'merged_ID_tkim2.csv'

with open(p3 / outfile_name, mode='w') as write_file:
    # csv의 headers(list형태)를 설정할 필요
    headers = []
    # header가 없으므로 일단 False
    outfile_has_header = False
    for filename in files:
        if '.txt' not in filename:
            continue
        read_file = open(p2 / filename, mode='r')
        # 각 파일의 contents를 list 형태로 담아야
        # 한 파일을 돌고 나면 contents는 다시 빈 list 형태로 변경
        contents = []
        for line in read_file.read().splitlines():
            splits = line.split(':')
            contents.append(splits[-1].strip())
            # 처음에는 len(headers)는 0이므로 실행 -> 그 후에는 len(contents) == len(headers)므로 미실행
            if len(contents) > len(headers):
                headers.append(splits[0].strip())
        # if not False -> if True
        if not outfile_has_header:
            header = ', '.join(headers)
            write_file.write(header)
            outfile_has_header = True
        new_line = ', '.join(contents)
        write_file.write(f'\n{new_line}')
    
print('Process Done!')
