Python 练习实例26
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**利用递归方法求5!。

**程序分析：**递归公式：fn=fn_1*4!

程序源代码：

实例
--
````
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  def  fact(j): sum = 0  if  j == 0: sum = 1  else: sum = j \* fact(j \- 1)  return  sum  print  fact(5)
```
以上实例输出结果为：
```
120
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)