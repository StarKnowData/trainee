Python 练习实例56
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**画图，学用circle画圆形。　　　

**程序分析：**无。

程序源代码：
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  if  \_\_name\_\_ == '\_\_main\_\_': from  Tkinter  import \* canvas = Canvas(width=800, height=600, bg='yellow')  canvas.pack(expand=YES, fill=BOTH)  k = 1  j = 1  for  i  in  range(0,26): canvas.create_oval(310 \- k,250 \- k,310 \+ k,250 \+ k, width=1)  k += j  j += 0.3  mainloop()
```
以上实例输出结果为：
```
![](http://www.runoob.com/wp-content/uploads/2015/10/circle.jpg)
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)