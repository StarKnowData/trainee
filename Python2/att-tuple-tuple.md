Python Tuple(元组) tuple()方法
==========================

[![Python 元组](../images/up.gif)Python 元组](python-tuples.html)

* * *

描述
--

Python 元组 tuple() 函数将列表转换为元组。

语法
--

tuple()方法语法：
```
tuple( seq )
```
参数
--

*   seq -- 要转换为元组的序列。

返回值
---

返回元组。

实例
--

以下实例展示了 tuple()函数的使用方法：
```
实例 1
----

>>>tuple([1,2,3,4])  (1, 2, 3, 4)  
>>> tuple({1:2,3:4})  #针对字典 会返回字典的key组成的tuple  (1, 3)  
>>> tuple((1,2,3,4))  #元组会返回元组自身  (1, 2, 3, 4)
```
```
实例 2
----

#!/usr/bin/python  

aList = \[123, 'xyz', 'zara', 'abc'\];   
aTuple = tuple(aList)    
print  "Tuple elements : ", aTuple
```
以上实例输出结果为：
```
Tuple elements :  (123, 'xyz', 'zara', 'abc')
```
[![Python 元组](../images/up.gif)Python 元组](python-tuples.html)