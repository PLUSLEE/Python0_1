# Python编程从入门到入土-（不完全）重要知识点

### 2.3.1使用方法修改字符串大小写

```python
.title()#首字母大写
.lower()#全小写
.upper()#全大写
```

### 2.3.3 使用制表符或换行符来添加空白

```python
\t #table功能
\n #换行
```

### 2.3.4 删除空白

```python
.rstrip() #删除末尾空白
.lstrip()#删除开头空白
.strip() #删除全部空白
```

### 2.4.1 整数

```python
3**2 #乘方：3^2=9
```

### 2.4.2 浮点数的处理

如何处理好浮点数的精度问题

```python
age = 23
message="Happy"+age+"rd Birthday!"#error
message="Happy"+str(age)+"rd Birthday!"#bingo
```

### 2.4.4 Python2中的整数

整数除法结果只包含整数部分。

```python
3/2     #1
3.0/2   #1.5
```

```python
>>> import this
# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
```

------------------

### 3.1.2 索引从0开始而不是1开始

访问列表最后一个元素

```python
list[-1]
```

### 3.2.2 在列表中添加元素

```python
list.append('list') #在末尾添加元素
list.insert(0,'list') #在指定位置添加元素
```

### 3.2.3 在列表中删除元素

```python
delet list[0] #使用delete删除指定位置的元素
element=list.pop() #‘弹出’列表中最后一个元素，并可以直接使用
element=list.pop(1) #弹出列表中指定位置的元素，并可以直接使用
list.remove('list') #根据列表中的值，删除元素
```


### 3.3 排序

```python 
.sort() #永久性排序
.sort(reverse=True) #永久性反转排序

sorted() #临时排序，不影响原列表
#注意大小写排序顺序有点复杂，但都基于以上方法

list.reverse()#反转列表顺序
list.reverse().reverse()#两次反转，list恢复原样

len(list) #确定列表长度
```

------------------

# 4操作列表

## 4.1 遍历整个列表

```python
for eachone in list:
    print(eachone)
```


### 4.3.1 使用函数range()

```python
for value in range(1,5): #包含头，不包含尾
    print(value)
```

### 4.3.3 对数字列表执行简单的统计计算

```python
numberList=[]
min(numberList) #最小值 
max(numberList) #最大值
sum(numberList) #总和
```


## 4.5元组
 
 不可变的列表称为元组。（速记：使用半圆形括号，括起来的列表，元素无法修改）

 虽然无法修改元组的元素，但是可以给存储元组的变量赋值。


 ### 5.2.5 检查多个条件

 ```python
argument1 >= number1 and argument2 <= number2
argument1 >= number1 or argument2 <= number2
 ```

 ### 5.2.6 检查特定值是否包含在列表中

 ```python
'element1' in list  # True or False
 ```

 
 ### 5.2.7 检查特定值是否包含在列表中

 ```python
if user not in users:
    print()
 ```


 # 6 字典

键--值

### 6.2.2 添加键值对
```python
alien_0={'color':'green,'points':5}
print(alien_0)

alien_0['x_position']=0
alien_0['y_position']=25
print(alien_0)
```

### 6.3.1 遍历键值对
```python
for key,value in dict.items():
    print(key)
    print(value)
```

### 6.3.2 遍历字典中所有的键

```python
for name in dict.keys():
    print(name.title())

```

### 6.3.3 遍历字典中所有的值

```python
for name in dict.values():
    print(name.title())
```


# 7用户输入和while循环

```python
message=input('message:') #输入文本信息
```