# -*- coding:utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)
from urllib.request import urlopen

# try:
#     # 2.X版本
#     from urllib2 import urlopen
# except:
#     from urllib.request import urlopen

import json

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

# 打印每一天的信息
for btc_dict in btc_data:
    date = btc_dict['date']
    month = btc_dict['month']
    week = btc_dict['week']
    weekday = btc_dict['weekday']
    close = btc_dict['close']
    print("{}is month {} week{},{},the close price is {} RMB".format(date, month, week, weekday, close))#格式化方式
