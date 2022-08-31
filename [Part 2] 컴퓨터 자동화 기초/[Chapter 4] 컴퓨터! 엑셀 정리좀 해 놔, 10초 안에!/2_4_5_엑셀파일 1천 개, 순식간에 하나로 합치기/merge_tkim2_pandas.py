from pathlib import Path
import os
import random
import openpyxl
import string
import shutil
import pandas as pd
import numpy as np

p1 = Path.home() / 'bhban_rpa-master' / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 4] 컴퓨터! 엑셀 정리좀 해 놔, 10초 안에!' / '2_4_4_예제용 엑셀파일 1천 개, 엔터키 한 번에 만들기' / 'personal_info_tkim2'
p2 = Path.home() / 'bhban_rpa-master' / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 4] 컴퓨터! 엑셀 정리좀 해 놔, 10초 안에!' / '2_4_5_엑셀파일 1천 개, 순식간에 하나로 합치기' / 'personal_info_tkim2'
p3 = Path.home() / 'bhban_rpa-master' / '[Part 2] 컴퓨터 자동화 기초' / '[Chapter 4] 컴퓨터! 엑셀 정리좀 해 놔, 10초 안에!' / '2_4_5_엑셀파일 1천 개, 순식간에 하나로 합치기'
try:
    shutil.copytree(p1, p2)
except:
    print('이미 존재하는 폴더입니다.')

# Path 객체의 glob() 함수 및 list comprehension, pandas concat() 함수를 결합하여 바로 진행 가능
merge_file = pd.concat([pd.read_excel(x) for x in p2.glob('*.xlsx')])
outfile_name = 'merged_ID_pandas_tkim2.xlsx'

xlsx_writer = pd.ExcelWriter(p3 / outfile_name)
merge_file.to_excel(xlsx_writer, sheet_name='total', index=False)
xlsx_writer.save()

print('Process Done!')