Python 练习实例87
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**回答结果（结构体变量传递）。

**程序分析：**无。

程序源代码：
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  if \_\_name\_\_ ==  '\_\_main\_\_':  class student: x =  0 c =  0  def f(stu): stu.x =  20 stu.c =  'c' a= student() a.x =  3 a.c =  'a' f(a)  print a.x,a.c
```
以上实例输出结果为：
```
20 c
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)