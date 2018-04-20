Python 练习实例55
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**学习使用按位取反~。

**程序分析：**~0=1; ~1=0;  
(1)先使a右移4位。  
(2)设置一个低4位全为1,其余全为0的数。可用~(~0<<4)  
(3)将上面二者进行&运算。

程序源代码：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

if \_\_name\_\_ == '\_\_main\_\_':
    a = 234
    b = ~a
    print 'The a\\'s 1 complement is %d' % b
    a = ~a
    print 'The a\\'s 2 complement is %d' % a
```
以上实例输出结果为：
```
The a's 1 complement is -235
The a's 2 complement is -235
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)