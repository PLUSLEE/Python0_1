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

print("Total repositories:", reponse_dict['total_count'])  # Total repositories: 4325746

# 探索有关仓库的信息
repo_dicts = reponse_dict['items']
print('Repositories returned:', len(repo_dicts))  # Repositories returned: 30

# 研究第一个仓库
# repo_dicts = repo_dicts[0]
# print('\nKeys:', len(repo_dicts))
# for key in sorted(repo_dicts.keys()):
#     print(key)

# 研究所有仓库
print('\nSelected information about first repository')
for repo_dict in repo_dicts:
    print('Name:', repo_dict['name'])
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])
