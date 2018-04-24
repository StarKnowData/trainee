Python 练习实例18
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。

**程序分析：**关键是计算出每一项的值。

程序源代码：
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  Tn = 0  Sn = \[\]  n = int(raw_input('n = '))  a = int(raw_input('a = '))  for  count  in  range(n): Tn = Tn \+ a  a = a \* 10  Sn.append(Tn)  print  Tn  Sn = reduce(lambda  x,y : x \+ y,Sn)  print  "计算和为：",Sn
```
以上实例输出结果为：
```
n = 4
a = 4
4
44
444
4444
计算和为： 4936
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)