Python 练习实例93
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**时间函数举例3。

**程序分析：**无。

程序源代码：
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  if \_\_name\_\_ ==  '\_\_main\_\_':  import time
    start = time.clock()  for i in range(10000):  print i end  = time.clock()  print  'different is %6.3f'  %  (end  - start)
```
以上实例输出结果为：
```
0  1  2  3  4  …… different is  0.014
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)