# -*- coding:utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)
from urllib.request import urlopen
import json
import math
import pygal
from itertools import groupby

# try:
#     # 2.X版本
#     from urllib2 import urlopen
# except:
#     from urllib.request import urlopen


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


# line_chart = pygal.Line(x_label_rotation=20,
#                         show_minor_x_labels=False)  # x_label_rotation=20,旋转20° ；show_minor_x_labels=False不用显示所有x轴标签
# line_chart.title = "收盘价（¥）"
# line_chart.x_labels = dates
# N = 20  # x坐标轴每隔20天显示一次
# line_chart.x_labels_major = dates[::N]
# close_log = [math.log10(_) for _ in close]  # 半对数变换，剔除非线性趋势，整体上涨趋势，更接近线性增长

# line_chart.add('收盘价', close)
# line_chart.add('收盘价', close_log)
# line_chart.render_to_file("收盘价折线图2（¥）.svg")


def draw_line(x_data, y_data, title, y_legend):
    xy_map = []  # 按月份、周数、周几分组，再计算每组的均值
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):  # 将x轴与y轴的数据合并、排序
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])
    x_unique, y_mean = [*zip(*xy_map)]
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')


# idx_month = dates.index('2017-12-01')
# line_chart_month = draw_line(months[:idx_month], close[:idx_month], '收盘价月日均值（¥）', '月日均值')
# line_chart_month
#
# idx_week = dates.index('2017-12-11')
# wd = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# weekdays_int = [wd.index(w) + 1 for w in weekdays[1:idx_week]]
# line_chart_weekday = draw_line(weekdays_int, close[1:idx_week], '收盘价星期均值（¥）', '星期均值')
# line_chart_weekday
# line_chart_weekday.x_labels = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
# line_chart_weekday.render_to_file('收盘价星期均值（¥）.svg')

# line_chart_week = draw_line(weeks[1:idx_week], close[1:idx_week], '收盘价周日均值（¥）', '周日均值')
# line_chart_week


# 收盘价数据仪表盘
with open('收盘价Dashboard.html', 'w', encoding='utf-8')as html_file:
    html_file.write('<html><head><title>收盘价DashBoard</title></title><meta charset="utf-8"</head><body>')
    for svg in ['收盘价折线图（¥）.svg', '收盘价月日均值（¥）.svg', '收盘价星期均值（¥）.svg', '收盘价周日均值（¥）.svg']:
        html_file.write('<object type="image/svg+xml" data="{0}">'
                        'height=500</object>\n'.format(svg))
    html_file.write('</body></html>')
