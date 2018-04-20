Python 练习实例28
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？

**程序分析：**利用递归的方法，递归分为回推和递推两个阶段。要想知道第五个人岁数，需知道第四人的岁数，依次类推，推到第一人（10岁），再往回推。

程序源代码：

实例
--
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  def  age(n): if  n == 1: c = 10  else: c = age(n \- 1) \+ 2  return  c  print  age(5)
```
以上实例输出结果为：
```
18
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)