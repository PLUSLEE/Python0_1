# -*- coding:utf-8 -*-

from DataVisualization.pygal.die import Die

# 创建一个D6
die = Die()

# 将结果保存在数组中
results = []
for roll in range(100):
    result = die.roll()
    results.append(result)
print(results)
