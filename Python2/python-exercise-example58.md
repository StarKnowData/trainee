Python 练习实例58
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**画图，学用rectangle画方形。　　　

**程序分析：**

rectangle(int left,  int top,  int right,  int bottom)

参数说明：(left ，top )为矩形的左上坐标，(right,bottom)为矩形的右下坐标，两者可确定一个矩形的大小
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  if  \_\_name\_\_ == '\_\_main\_\_': from  Tkinter  import \* root = Tk()  root.title('Canvas')  canvas = Canvas(root,width = 400,height = 400,bg = 'yellow')  x0 = 263  y0 = 263  y1 = 275  x1 = 275  for  i  in  range(19): canvas.create_rectangle(x0,y0,x1,y1)  x0 -= 5  y0 -= 5  x1 += 5  y1 += 5  canvas.pack()  root.mainloop()
```
以上实例输出结果为：

![](http://www.runoob.com/wp-content/uploads/2015/10/tk3.jpg)

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)