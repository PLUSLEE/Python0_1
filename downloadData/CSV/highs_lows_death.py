# -*- coding:utf-8 -*-

"""
错误检查
"""

import csv
from matplotlib import pyplot as plt
from datetime import datetime

filename = 'death_valley_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 调用read一次，只读取一行csv
    print(header_row)

    for index, column_header in enumerate(header_row):  # 获取每个元素的索引和值
        print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])  # 读取csv对应index的值，同时将字符串转换为数字int；如果碰到了空白字符串就会报错，需要修正
            low = int(row[3])
        except ValueError:  # 缺少数据，使用except ValueError来排除错误，使程序正常运行下去
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
    print(highs)

# 根据数据绘制图形
fig = plt.figure(dpi=300, figsize=(10, 6))
plt.plot(dates, highs, c='red', alpha=0.5)
plt.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形格式
plt.title("Daily high and low temperatures, 2014 \nDeath Vally,CA", fontsize=24)
plt.xlabel('', fontsize=16)
plt.ylabel("Temperature (F)", fontsize=16)
fig.autofmt_xdate()
plt.tick_params(axis='both', which='major', labelsize=16)

plt.savefig('high_low_death_vally.png', bbox_inches="tight")
plt.show()
