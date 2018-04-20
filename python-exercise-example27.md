Python 练习实例27
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。

**程序分析：**无。

程序源代码：
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  def  output(s,l): if  l==0: return  print  (s\[l-1\])  output(s,l-1)  s = raw_input('Input a string:')  l = len(s)  output(s,l)
```
以上实例输出结果为：
```
Input a string:abcde
e
d
c
b
a
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)```