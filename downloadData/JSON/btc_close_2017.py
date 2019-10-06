# -*- coding:utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)
from urllib.request import urlopen

# try:
#     # 2.X版本
#     from urllib2 import urlopen
# except:
#     from urllib.request import urlopen

import json
import pygal

# json_url = 'http://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
# response = urlopen(json_url)
# print(response)
#
# # 读取数据
# req = response.read()
# print(req)
#
# # 将数据写入文件
# # with open('btc_close_2017_urllib.json', 'wb')as f:
# #     f.write(req)
#
# # 加载json格式
# # file_urllib = json.load(req)  # 'bytes' object has no attribute 'read'
# file_urllib = json.loads(req)
# print(file_urllib)

# 将数据加载到一个列表中
filename = 'btc_close_2017.json'
with open(filename)as f:
    btc_data = json.load(f)

# 创建5个列表，分别存储日期和收盘价
dates = []
months = []
weeks = []
weekdays = []
close = []

# 打印每一天的信息
# for btc_dict in btc_data:
#     date = btc_dict['date']
#     month = int(btc_dict['month'])
#     week = int(btc_dict['week'])
#     weekday = btc_dict['weekday']
#     # close = int(btc_dict['close'])  # Python 不能直接将包含小数点的字符串转换为整数；正确操作：先转换为浮点数，再将浮点数转换为整数。
#     close = int(float(btc_dict['close']))
#     print("{}is month {} week{},{},the close price is {} RMB".format(date, month, week, weekday, close))  # 格式化方式

for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))

line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)#x_label_rotation=20,旋转20° ；show_minor_x_labels=False不用显示所有x轴标签
line_chart.title = "收盘价（¥）"
line_chart.x_labels = dates
N = 20  # x坐标轴每隔20天显示一次
line_chart.x_labels_major = dates[::N]
line_chart.add('收盘价', close)
line_chart.render_to_file("收盘价折线图（¥）.svg")
