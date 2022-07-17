from pathlib import Path
import time
import random
import shutil
import os
# pandas 라이브러리 활용하여 시도
import pandas as pd

# 폴더를 복사하는 것부티 진행 -> shutil모듈 활용(copytree)
p1 = Path.cwd() / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 4] 컴퓨터! 엑셀 정리좀 해 놔, 10초 안에!' / '2_4_4_예제용 엑셀파일 1천 개, 엔터키 한 번에 만들기' / 'personal_info_tkim1'
p2 = Path.cwd() / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 4] 컴퓨터! 엑셀 정리좀 해 놔, 10초 안에!' / '2_4_5_엑셀파일 1천 개, 순식간에 하나로 합치기' / 'personal_info_tkim1'
p3 = Path.cwd() / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 4] 컴퓨터! 엑셀 정리좀 해 놔, 10초 안에!' / '2_4_5_엑셀파일 1천 개, 순식간에 하나로 합치기'
try:
    shutil.copytree(p1, p2)
except:
    print('이미 존재하는 폴더입니다.')

files = os.listdir(p2)
outfile_name = 'merged_ID_pandas_tkim1.xlsx'

file_list = []
for i, filename in enumerate(files):
    file_df = pd.read_excel(p2 / filename)
    file_list.append(file_df)

file_dfs = pd.concat(file_list)

xlsx_writer = pd.ExcelWriter(p3 / outfile_name)
file_dfs.to_excel(xlsx_writer, sheet_name='Total', index=False)
xlsx_writer.save()

print('Process Done!')