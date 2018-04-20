Python 练习实例19
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。

**程序分析：**请参照程序[Python 练习实例14](python-exercise-example14.html)。

程序源代码：
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  from  sys  import  stdout  for  j  in  range(2,1001): k = \[\]  n = -1  s = j  for  i  in  range(1,j): if  j % i == 0: n += 1  s -= i  k.append(i)  if  s == 0: print  j  for  i  in  range(n): stdout.write(str(k\[i\]))  stdout.write('  ')  print  k\[n\]
```
以上实例输出结果为：
```
6
1 2 3
28
1 2 4 7 14
496
1 2 4 8 16 31 62 124 248
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)