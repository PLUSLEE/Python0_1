# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt

from DataVisualization.random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=6)
    # plt.scatter(rw.x_value, rw.y_value, s=15)

    plt.scatter(0, 0, c='green', edgecolors='none', s=50)  # 起点
    plt.scatter(rw.x_value[-1], rw.y_value[-1], c='red', edgecolors='none', s=50)  # 终点

    #隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
