# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt  # as为指定别名，避免反复输入pyplot

squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth=5)

# 设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel('Square of Value', fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()