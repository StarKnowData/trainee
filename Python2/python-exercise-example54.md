Python 练习实例54
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**取一个整数a从右端开始的4〜7位。

**程序分析：**可以这样考虑：  
(1)先使a右移4位。  
(2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4)  
(3)将上面二者进行&运算
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  if  \_\_name\_\_ == '\_\_main\_\_': a = int(raw_input('input a number:\\n'))  b = a >\> 4  c = ~(~0 << 4)  d = b & c  print  '%o\\t%o' %(a,d)
```
以上实例输出结果为：
```
input a number:
9
11    0
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)