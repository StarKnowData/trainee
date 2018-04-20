Python shuffle() 函数
===================

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

**shuffle()** 方法将序列的所有元素随机排序。

* * *

语法
--

以下是 shuffle() 方法的语法:
```
import random

random.shuffle (lst )
```
**注意：**shuffle()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。

* * *

参数
--

*   lst -- 可以是一个序列或者元组。

* * *

返回值
---

返回随机排序后的序列。

* * *

实例
--

以下展示了使用 shuffle() 方法的实例：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import random

list = [20, 16, 10, 5];
random.shuffle(list)
print "随机排序列表 : ",  list

random.shuffle(list)
print "随机排序列表 : ",  list
```
以上实例运行后输出结果为：
```
随机排序列表 :  [16, 5, 10, 20]
随机排序列表 :  [16, 5, 20, 10]
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)