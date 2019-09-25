# -*- coding:utf-8 -*-

from __future__ import (absolute_import, division, print_function, unicode_literals)
import requests


json_url = 'http://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)
# 将数据写入文件
with open('btc_close_2017_request.json', 'w')as f:
    f.write(req.text)
file_requests = req.json()


