'''
在图表中添加可点击的链接
'''

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

names, plot_dicts = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])

    plot_dict = {
        'value': repo_dict['stargazers_count'],
        'label': str(repo_dict['description']),
        'xlink': repo_dict['html_url']  # 添加可点击的链接
        # 'label': repo_dict['description']  AttributeError: 'NoneType' object has no attribute 'decode'
        # 'value': repo_dict['description']  TypeError: '<' not supported between instances of 'int' and 'str'
    }

    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#ff4040', base_style=LCS)

'''
改进可视化,通过config进行设置
'''

my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.turncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)

# chart = pygal.Bar(style=my_style, x_lable_rotation=45, show_legend=False)  # x_label旋转45度失效，legend图例显示
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', plot_dicts)
chart.render_to_file('python_repos6.svg')
