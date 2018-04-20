Python 练习实例10
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**暂停一秒输出，并格式化当前时间。

**程序分析：**无。

程序源代码：
```
实例(Python 2.0+)
---------------

#!/usr/bin/python 
\# -*- coding: UTF-8 -*- 
import  time  print  time.
strftime('%Y-%m-%d %H:%M:%S',time.
localtime(time.time()))  
\# 暂停一秒 
time.sleep(1) 
print  time.
strftime('%Y-%m-%d %H:%M:%S',time.

localtime(time.time()))
```
以上实例输出结果为：
```
2015-10-21  17:48:40  2015-10-21  17:48:41
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)