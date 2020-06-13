"""
python에서 데이터 분석을 할 때 자주 사용되는 패키지:
    numpy, pandas, matplotlib, cipy

"""

from pandas.io.parsers import read_csv
import matplotlib.pyplot as plt   # 그래프를 위한 라이브러리

# csv 파일에서 data frame 만들기

df = read_csv('csv_exam.csv')

print('Type:', type(df))  # 데이터 프레임의 row(observation)의 갯수
print('Shape:', df.shape)  # 데이터 프레임의 (row, col)
print('Head:\n', df.head(3))  # 데이터 프레임의 처음 일부 데이터
print('tail:\n', df.tail(3))
print('Values:\n', df.values)
print('Describe:\n', df.describe())  # 요약 통계량(최솟값, 최댓값, 중앙값, 평균 ...)

print('-'*30)