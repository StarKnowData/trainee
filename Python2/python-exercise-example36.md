Python 练习实例36
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**求100之内的素数。

**程序分析：**无。

程序源代码：
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  \# 输出指定范围内的素数  \# 用户输入数据  lower = int(input("输入区间最小值: "))  upper = int(input("输入区间最大值: "))  for  num  in  range(lower,upper \+ 1): \# 素数大于 1  if  num \> 1: for  i  in  range(2,num): if  (num % i) == 0: break  else: print(num)
```
以上实例输出结果为：
```
输入区间最小值: 1
输入区间最大值: 100
2
3
5
7
11
13
17
19
23
29
31
37
41
43
47
53
59
61
67
71
73
79
83
89
97
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)