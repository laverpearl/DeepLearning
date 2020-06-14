import matplotlib.pyplot as plt

data = [[2,0], [4,0], [6,0], [8,1], [10,1], [12,1], [14,1]]

x_data = [i[0] for i in data] #勉強した時間
y_data = [i[1] for i in data] #合格

plt.scatter(x_data, y_data) #그래프 설정
plt.xlim(0, 15)
plt.ylim(-.1, 1.1)

plt.show()