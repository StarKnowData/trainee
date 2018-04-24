Python 练习实例47
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**两个变量值互换。

**程序分析：**无

程序源代码：
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  def  exchange(a,b): a,b = b,a  return  (a,b)  if  \_\_name\_\_ == '\_\_main\_\_': x = 10  y = 20  print  'x = %d,y = %d' % (x,y)  x,y = exchange(x,y)  print  'x = %d,y = %d' % (x,y)
```
以上实例输出结果为：
```
x =  10,y =  20 x =  20,y =  10
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)