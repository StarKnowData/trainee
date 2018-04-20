Python 练习实例49
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**使用lambda来创建匿名函数。

**程序分析：**无

实例
--
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  MAXIMUM = lambda  x,y : (x \> y) \* x \+ (x < y) \* y  MINIMUM = lambda  x,y : (x \> y) \* y \+ (x < y) \* x  if  \_\_name\_\_ == '\_\_main\_\_': a = 10  b = 20  print  'The largar one is %d' % MAXIMUM(a,b)  print  'The lower one is %d' % MINIMUM(a,b)
```
以上实例输出结果为：
```
The largar one is 20
The lower one is 10
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)