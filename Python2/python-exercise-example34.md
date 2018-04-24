Python 练习实例34
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**练习函数调用。

**程序分析：**无。

实例
--
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  def  hello_world(): print  'hello world'  def  three_hellos(): for  i  in  range(3): hello_world()  if  \_\_name\_\_ == '\_\_main\_\_': three_hellos()
```
以上实例输出结果为：
```
hello world
hello world
hello world
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)