from pathlib import Path
import time
import random
import shutil
import os
# csv모듈을 활용하여 생성 시도 -> 책과는 관계 없이 내가 생각하는 방향으로
import csv
import pandas as pd

p1 = Path.home() / 'bhban_rpa-master' / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 4] 컴퓨터! 엑셀 정리좀 해 놔, 10초 안에!' / '2_4_1_예제용 CSV 파일 1천 개, 1초만에 만들기' / 'personal_info_tkim2'
p2 = Path.home() / 'bhban_rpa-master' / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 4] 컴퓨터! 엑셀 정리좀 해 놔, 10초 안에!' / '2_4_3_CSV파일 1천 개, 양식을 유지하며 하나로 합치기' / 'personal_info_tkim2'
p3 = Path.home() / 'bhban_rpa-master' / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 4] 컴퓨터! 엑셀 정리좀 해 놔, 10초 안에!' / '2_4_3_CSV파일 1천 개, 양식을 유지하며 하나로 합치기'
try:
    shutil.copytree(p1, p2)
except:
    print('이미 존재하는 폴더입니다.')

# 이렇게 진행할 경우 encoding 문제 발생 -> 엑셀을 열어 다른 이름으로 저장을 해줘야하는데.. 숫자가 많으면 어려울듯
# 그럼 csv 파일 자체 encoding을 바꿔버리면 될듯?
merge_file = pd.concat([pd.read_csv(x, engine='python') for x in p2.glob('*.csv')])

merge_file.to_csv(p3 / 'merged_ID_tkim3.csv', index=False)

print('Process Done!')