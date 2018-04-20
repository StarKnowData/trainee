Python 练习实例64
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**利用ellipse 和 rectangle 画图。。　

**程序分析：**无。

程序源代码：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

if \_\_name\_\_ == '\_\_main\_\_':
    from Tkinter import *
    canvas = Canvas(width = 400,height = 600,bg = 'white')
    left = 20
    right = 50
    top = 50
    num = 15
    for i in range(num):
        canvas.create_oval(250 - right,250 - left,250 + right,250 + left)
        canvas.create_oval(250 - 20,250 - top,250 + 20,250 + top)
        canvas.create_rectangle(20 - 2 * i,20 - 2 * i,10 * (i + 2),10 * ( i + 2))
        right += 5
        left += 5
        top += 10
```
    canvas.pack()
    mainloop()

以上实例输出结果为：

![](http://www.runoob.com/wp-content/uploads/2015/10/tk6.jpg)

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)