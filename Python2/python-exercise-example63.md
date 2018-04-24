Python 练习实例63
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**画椭圆。　

**程序分析：**使用 Tkinter。

程序源代码：

实例
--
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  if  \_\_name\_\_ == '\_\_main\_\_': from  Tkinter  import \* x = 360  y = 160  top = y \- 30  bottom = y \- 30  canvas = Canvas(width = 400,height = 600,bg = 'white')  for  i  in  range(20): canvas.create_oval(250 \- top,250 \- bottom,250 \+ top,250 \+ bottom)  top -= 5  bottom += 5  canvas.pack()  mainloop()
```
以上实例输出结果为：

![](http://www.runoob.com/wp-content/uploads/2015/10/tk5.jpg)

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)