Python 练习实例25
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**求1+2!+3!+...+20!的和。

**程序分析：**此程序只是把累加变成了累乘。

方法一
---
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  n = 0  s = 0  t = 1  for  n  in  range(1,21): t *= n  s += t  print  '1! + 2! + 3! + ... + 20! = %d' % s
```
方法二
---
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  s = 0  l = range(1,21)  def  op(x): r = 1  for  i  in  range(1,x \+ 1): r *= i  return  r  s = sum(map(op,l))  print  '1! + 2! + 3! + ... + 20! = %d' % s
```
以上实例输出结果为：
```
1! + 2! + 3! + ... + 20! = 2561327494111820313
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)