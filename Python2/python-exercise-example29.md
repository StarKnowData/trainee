Python 练习实例29
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。

**程序分析：**学会分解出每一位数。

程序源代码：

实例
--
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  x = int(raw_input("请输入一个数:\\n"))  a = x / 10000  b = x % 10000 / 1000  c = x % 1000 / 100  d = x % 100 / 10  e = x % 10  if  a != 0: print  "5 位数：",e,d,c,b,a  elif  b != 0: print  "4 位数：",e,d,c,b, elif  c != 0: print  "3 位数：",e,d,c  elif  d != 0: print  "2 位数：",e,d  else: print  "1 位数：",e
```
以上实例输出结果为：
```
请输入一个数:  23459  5  位数：  9  5  4  3  2

请输入一个数:  3472  4  位数：  2  7  4  3
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)