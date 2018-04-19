Python 字典(Dictionary) setdefault()方法

描述

Python 字典 setdefault() 函数和get() 方法类似, 如果键不存在于字典中，将会添加键并将值设为默认值。

语法

setdefault()方法语法：

dict.setdefault(key, default=None)
参数

key -- 查找的键值。
default -- 键不存在时，设置的默认键值。
返回值

如果字典中包含有给定键，则返回该键对应的值，否则返回为该键设置的值。

实例

以下实例展示了 setdefault() 函数的使用方法：

实例(Python 2.0+)

#!/usr/bin/python    
\# -*- coding: UTF-8 -*- 

dict = {'runoob': '菜鸟教程', 'google': 'Google 搜索'}   

print  "Value : %s" %   
dict.setdefault('runoob', None)   
print  "Value : %s" %   
dict.setdefault('Taobao', '淘宝')
以上实例输出结果为：

Value : 菜鸟教程
Value : 淘宝
