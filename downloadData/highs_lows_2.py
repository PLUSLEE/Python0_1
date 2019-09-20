# -*- coding:utf-8 -*-

import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中获取最高气温
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 调用read一次，只读取一行csv
    # print(header_row)

    for index, column_header in enumerate(header_row):  # 获取每个元素的索引和值
        print(index, column_header)

    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[0], "%Y-%m-%d")
        dates.append(current_date)

        high = int(row[1])  # 读取csv对应index的值，同时将字符串转换为数字int
        highs.append(high)

    print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=300, figsize=(10, 6))
plt.plot(dates, highs, c='red')

# 设置图形格式
plt.title("Daily high temperatures, 2014", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig('high_low_2.png', bbox_inches="tight")
plt.show()
