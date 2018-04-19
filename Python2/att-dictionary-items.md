Python 字典(Dictionary) items()方法

描述

Python 字典(Dictionary) items() 函数以列表返回可遍历的(键, 值) 元组数组。

语法

items()方法语法：

dict.items()
参数

NA。
返回值

返回可遍历的(键, 值) 元组数组。

实例

以下实例展示了 items()函数的使用方法：

实例(Python 2.0+)

#!/usr/bin/python  
\# coding=utf-8  

dict = {'Google': 'www.google.com', 'Runoob': 'www.runoob.com', 'taobao': 'www.taobao.com'}  

print  "字典值 : %s" % dict.items()  

\# 遍历字典列表   
for  key,values  in  dict.items(): 
print  key,values  
以上实例输出结果为：

字典值 : \[('Google', 'www.google.com'), ('taobao', 'www.taobao.com'), ('Runoob', 'www.runoob.com')\]
Google www.google.com
taobao www.taobao.com
Runoob www.runoob.com  
