Python 练习实例53
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**学习使用按位异或 ^ 。

**程序分析：**0^0=0; 0^1=1; 1^0=1; 1^1=0

程序源代码：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

if \_\_name\_\_ == '\_\_main\_\_':
    a = 077
    b = a ^ 3
    print 'The a ^ 3 = %d' % b
    b ^= 7
    print 'The a ^ b = %d' % b
```
以上实例输出结果为：
```
The a ^ 3 = 60
The a ^ b = 59
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)