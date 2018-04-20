Python 练习实例85
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。

**程序分析：**999999 / 13 = 76923。

程序源代码：

实例
--
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  if  \_\_name\_\_ == '\_\_main\_\_': zi = int(raw_input('输入一个数字:\\n'))  n1 = 1  c9 = 1  m9 = 9  sum = 9  while  n1 != 0: if  sum % zi == 0: n1 = 0  else: m9 *= 10  sum += m9  c9 += 1  print  '%d 个 9 可以被 %d 整除 : %d' % (c9,zi,sum)  r = sum / zi  print  '%d / %d = %d' % (sum,zi,r)
```
以上实例输出结果为：
```
输入一个数字:  13  6  个  9  可以被  13  整除  :  999999  999999  /  13  =  76923
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)