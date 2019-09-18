# -*- coding:utf-8 -*-

from DataVisualization.pygal.die import Die
import pygal

# 创建一个D6
die = Die()

# 将结果保存在数组中
results = []
for roll in range(1000):
    result = die.roll()
    results.append(result)
# print(results)

frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)  # 统计results中结果在1-6的值；统计思路：先统计results中1的个数，再统计2，依次类推；
    frequencies.append(frequency)
# print(frequencies)

# 对结果进行可视化
hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('div_visual.svg')
