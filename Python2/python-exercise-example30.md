Python 练习实例30
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。

**程序分析：**无。

程序源代码：
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  a = int(raw_input("请输入一个数字:\\n"))  x = str(a)  flag = True  for  i  in  range(len(x)/2): if  x\[i\] != x\[-i \- 1\]: flag = False  break  if  flag: print  "%d 是一个回文数!" % a  else: print  "%d 不是一个回文数!" % a
```
以上实例输出结果为：
```
请输入一个数字:
12321
12321 是一个回文数!
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)