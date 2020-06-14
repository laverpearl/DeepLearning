import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#勉強時間 xと合否　yの　リストを　作る。
data = [[2,0], [4,0], [6,0], [8,1], [10,1], [12,1], [14,1]]

x_data = [i[0] for i in data] #勉強した時間
y_data = [i[1] for i in data] #合否

#그래프로 나타내
plt.scatter(x_data, y_data)
plt.xlim(0, 15)
plt.ylim(-.1, 1.1)

#aとbの値を初期化して、lrを決める。
a = 0 #傾き
b = 0
lr = 0.05 #学習率

def sigmoid(x): #sigmoidと言う関数を定義。
    return 1 / (1 + np.e ** (-x)) #sigmoidの形　そのまま　pythonに移す。

#경사 하강법 실행
#1000번 반복될 때마다 각 x_data 값에 대한 현재의 a값, b값 출력
for i in range(2001):
    for x_data, y_data in data:
        a_diff = x_data*(sigmoid(a * x_data + b) - y_data)
        b_diff = sigmoid(a * x_data + b) - y_data
        a = a - lr * a_diff
        b = b - lr * b_diff
        if i % 1000 == 0:
            print("epoch=%.f, 기울기=%.04f, 절편=%.04f" % (i, a, b))
        plt.scatter(x_data, y_data)
        plt.xlim(0, 15)
        plt.ylim(-.1, 1.1)
        x_range = (np.arange(0, 15, 0.1)) #그래프로 나타낼 x값의 범위 정하기
        plt.plot(np.arange(0, 15, 0.1), np.array([sigmoid(a * x + b) for x in x_range]))



        #plt.show()







