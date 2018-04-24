Python 练习实例69
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。

**程序分析：**无。

程序源代码：
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  if  \_\_name\_\_ == '\_\_main\_\_': nmax = 50  n = int(raw_input('请输入总人数:'))  num = \[\]  for  i  in  range(n): num.append(i \+ 1)  i = 0  k = 0  m = 0  while  m < n \- 1: if  num\[i\] != 0 : k += 1  if  k == 3: num\[i\] = 0  k = 0  m += 1  i += 1  if  i == n : i = 0  i = 0  while  num\[i\] == 0: i += 1  print  num\[i\]
```
执行以上代码，输出结果：
```
$ python test.py 请输入总人数:34  10
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)