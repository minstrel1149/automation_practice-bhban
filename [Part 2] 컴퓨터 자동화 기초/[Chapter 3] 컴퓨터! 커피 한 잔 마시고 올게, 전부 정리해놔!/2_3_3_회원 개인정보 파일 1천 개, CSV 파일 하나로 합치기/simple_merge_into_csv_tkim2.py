from pathlib import Path
import os
import shutil

p1 = Path.home() / 'bhban_rpa-master' / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 3] 컴퓨터! 커피 한 잔 마시고 올게, 전부 정리해놔!' / '2_3_2_회원 개인정보 파일 1천 개, 텍스트 파일 하나로 합치기' / 'personal_info_tkim2'
p2 = Path.home() / 'bhban_rpa-master' / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 3] 컴퓨터! 커피 한 잔 마시고 올게, 전부 정리해놔!' / '2_3_3_회원 개인정보 파일 1천 개, CSV 파일 하나로 합치기' / 'personal_info_tkim2'
p3 = Path.home() / 'bhban_rpa-master' / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 3] 컴퓨터! 커피 한 잔 마시고 올게, 전부 정리해놔!' / '2_3_3_회원 개인정보 파일 1천 개, CSV 파일 하나로 합치기'
try:
    shutil.copytree(p1, p2)
except:
    print('이미 존재하는 폴더입니다.')

outfile_name = 'merged_ID_tkim2.csv'

files = os.listdir(p2)

# 원래는 for문 안에 write파일을 넣었었는데, 밖으로 빼는게 더 좋은 것 같아 수정
with open(p3 / outfile_name, mode='w') as write_file:
    for filename in files:
        if '.txt' not in filename:
            continue
        read_file = open(p2 / filename, mode='r')
        contents = read_file.read()
        write_file.write(f'{contents}\n\n')

print('Process Done!')