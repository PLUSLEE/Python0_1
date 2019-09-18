# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt

from DataVisualization.random_walk import RandomWalk

while True:
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_value, rw.y_value, s=15)
    plt.show()

    keep_running = input("Make another walk?(y/n):")
    if keep_running == 'n':
        break
