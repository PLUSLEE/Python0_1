# -*- coding:utf-8 -*-

import requests

# 执行API调用并存储响应
url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code:", r.status_code)  # Status Code: 200

# 将API响应存储在一个变量中
reponse_dict = r.json()

# 处理结果
print(reponse_dict.keys())  # dict_keys(['total_count', 'incomplete_results', 'items'])
