Python 练习实例40
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**将一个数组逆序输出。

**程序分析：**用第一个与最后一个交换。

程序源代码：
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  if  \_\_name\_\_ == '\_\_main\_\_': a = \[9,6,5,4,1\]  N = len(a)  print  a  for  i  in  range(len(a) / 2): a\[i\],a\[N \- i \- 1\] = a\[N \- i \- 1\],a\[i\]  print  a
```
以上实例输出结果为：
```
\[9, 6, 5, 4, 1\]
\[1, 4, 5, 6, 9\]
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)