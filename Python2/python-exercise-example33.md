Python 练习实例33
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**按逗号分隔列表。

**程序分析：**无。
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  L = \[1,2,3,4,5\]  s1 = ','.join(str(n)  for  n  in  L)  print  s1
```
以上实例输出结果为：
```
1,2,3,4,5
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)