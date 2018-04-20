Python 练习实例52
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**学习使用按位或 | 。

**程序分析：**0|0=0; 0|1=1; 1|0=1; 1|1=1
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  if  \_\_name\_\_ == '\_\_main\_\_': a = 077  b = a | 3  print  'a | b is %d' % b  b |= 7  print  'a | b is %d' % b
```
以上实例输出结果为：
```
a | b is  63 a | b is  63
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)