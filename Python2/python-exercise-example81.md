Python 练习实例81
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。

**程序分析：**无。

程序源代码：
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  a = 809  for  i  in  range(10,100): b = i \* a  if  b >= 1000  and  b <= 10000  and  8 \* i < 100  and  9 \* i >= 100: print  b,' = 800 * ', i, ' \+ 9 * ', i
```
以上实例输出结果为：
```
9708  =  800  *  12  +  9  *  12
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)