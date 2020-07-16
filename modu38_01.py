# 왜 오류가 나는지 모르겠다 /// 모두의딥러닝 110p

import numpy as np

fake_a_b = [3, 76]

data = [[2, 81], [4, 93], [6, 91], [8, 97]]
x = [i[0] for i in data]
y = [i[1] for i in data]

def predict(x):
    return fake_a_b[0]*x + fake_a_b[1]

def mse(y_hat, y):
    return ((y_hat, y) ** 2).mean()

def mse_val(predict_result, y):
    return mse(np.array(predict_result), np.array(y))

predict_result = []

for i in range(len(x)):
    predict_result.append(predict(x[i]))
    print("勉強した時間　=　%.f, 実際の点数 = %.f, 様相点数 = %.f" % (x[i], y[i], predict(x[i])))

print("mse 値 : " + str(mse_val(predict_result, y)))







