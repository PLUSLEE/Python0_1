# -*- coding:utf-8 -*-

import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 调用read一次，只读取一行csv
    # print(header_row)

    for index, column_header in enumerate(header_row):  # 获取每个元素的索引和值
        print(index, column_header)

    highs = []
    for row in reader:
        highs.append(row[1])  # 读取csv对应index的值

    print(highs)
