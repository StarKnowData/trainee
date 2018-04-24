Python 练习实例57
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**画图，学用line画直线。

**程序分析：**无。

实例
--
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  if  \_\_name\_\_ == '\_\_main\_\_': from  Tkinter  import \* canvas = Canvas(width=300, height=300, bg='green')  canvas.pack(expand=YES, fill=BOTH)  x0 = 263  y0 = 263  y1 = 275  x1 = 275  for  i  in  range(19): canvas.create_line(x0,y0,x0,y1, width=1, fill='red')  x0 = x0 \- 5  y0 = y0 \- 5  x1 = x1 \+ 5  y1 = y1 \+ 5  x0 = 263  y1 = 275  y0 = 263  for  i  in  range(21): canvas.create_line(x0,y0,x0,y1,fill = 'red')  x0 += 5  y0 += 5  y1 += 5  mainloop()
```
以上实例输出结果为：

![](http://www.runoob.com/wp-content/uploads/2015/10/line.jpg)

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)