# -*- coding:utf-8 -*-

from DataVisualization.pygal.die import Die
import pygal

# 创建两个D6
die1 = Die()
die2 = Die()

# 将结果保存在数组中
results = []
for roll in range(1000):
    result = die1.roll() + die2.roll()
    results.append(result)
# print(results)

frequencies = []
# for value in range(1, die.num_sides + 1):
#     frequency = results.count(value)  # 统计results中结果在1-6的值；统计思路：先统计results中1的个数，再统计2，依次类推；
#     frequencies.append(frequency)
# print(frequencies)
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化
hist = pygal.Bar()  # 直方图
hist.title = "Results of rolling two D6 1000 times"
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D6', frequencies)  # 添加图例
hist.render_to_file('div_visual_2.svg')
