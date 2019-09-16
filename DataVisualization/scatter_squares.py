# -*- coding:utf-8 -*-

import matplotlib.pyplot as plt

# x_values=[1,2,3,4,5]
# y_values=[1,4,9,16,25]
# plt.scatter(x_values,y_values,s=200)

x_values = list(range(1, 1001))
y_values = [x ** 2 for x in x_values]

# plt.scatter(x_values, y_values, c='red', edgecolors='none', s=5)  # 删除数据点轮廓,设置数据点颜色
# plt.scatter(x_values, y_values, c=(1, 0, 0.8), edgecolors='none', s=5)  # 删除数据点轮廓,使用RGB设置数据点颜色
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none',
            s=40)  # c设置为y值列表，使用cmap告诉pyplot使用哪个颜色映射

# 设置图表标题并给坐标轴加上标签
plt.title("Square Nubers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.savefig('squares_plot.png', bbox_inches="tight")  # 参数二，裁减掉空白区域，这句代码放在plt.show()前面，否则不能正常保存图像
plt.show()
