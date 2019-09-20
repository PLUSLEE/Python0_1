# -*- coding:utf-8 -*-

import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)  # 调用read一次，只读取一行csv
    print(header_row)
