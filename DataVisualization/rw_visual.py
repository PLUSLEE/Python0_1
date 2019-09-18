# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt

from DataVisualization.random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_value, rw.y_value, c=point_numbers, cmap=plt.cm.Reds, edgecolors='none', s=6)
    # plt.scatter(rw.x_value, rw.y_value, s=15)
    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
