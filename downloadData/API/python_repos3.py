# -*- coding:utf-8 -*-

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'http://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print("Status Code:", r.status_code)  # Status Code: 200

# 将API响应存储在一个变量中
reponse_dict = r.json()

# 处理结果
print(reponse_dict.keys())  # dict_keys(['total_count', 'incomplete_results', 'items'])

print("Total repositories:", reponse_dict['total_count'])  # Total repositories: 4325746

# 探索有关仓库的信息
repo_dicts = reponse_dict['items']
print('Repositories returned:', len(repo_dicts))  # Repositories returned: 30

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
my_style = LS('#ff4040', base_style=LCS)
chart = pygal.Bar(style=my_style, x_lable_rotation=45, show_legend=False)  # x_label旋转45度失效，legend图例显示
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', stars)
chart.render_to_file('python_repos.svg')

# 研究第一个仓库
# repo_dicts = repo_dicts[0]
# print('\nKeys:', len(repo_dicts))
# for key in sorted(repo_dicts.keys()):
#     print(key)

# 研究所有仓库
# print('\nSelected information about first repository')
# for repo_dict in repo_dicts:
#     print('Name:', repo_dict['name'])
#     print('Owner:', repo_dict['owner']['login'])
#     print('Stars:', repo_dict['stargazers_count'])
#     print('Repository:', repo_dict['html_url'])
#     print('Created:', repo_dict['created_at'])
#     print('Updated:', repo_dict['updated_at'])
#     print('Description:', repo_dict['description'])
