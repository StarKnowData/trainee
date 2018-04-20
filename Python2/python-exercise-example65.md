Python 练习实例65
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**一个最优美的图案。　　

**程序分析：**无。

程序源代码：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import math
class PTS:
    def \_\_init\_\_(self):
        self.x = 0
        self.y = 0
points = \[\]

def LineToDemo():
    from Tkinter import *
    screenx = 400
    screeny = 400
    canvas = Canvas(width = screenx,height = screeny,bg = 'white')

    AspectRatio = 0.85
    MAXPTS = 15
    h = screeny
    w = screenx
    xcenter = w / 2
    ycenter = h / 2
    radius = (h - 30) / (AspectRatio * 2) - 20
    step = 360 / MAXPTS
    angle = 0.0
    for i in range(MAXPTS):
        rads = angle * math.pi / 180.0
        p = PTS()
        p.x = xcenter + int(math.cos(rads) * radius)
        p.y = ycenter - int(math.sin(rads) * radius * AspectRatio)
        angle += step
        points.append(p)
    canvas.create_oval(xcenter - radius,ycenter - radius,
                       xcenter + radius,ycenter + radius)
    for i in range(MAXPTS):
        for j in range(i,MAXPTS):
            canvas.create_line(points\[i\].x,points\[i\].y,points\[j\].x,points\[j\].y)

    canvas.pack()
    mainloop()
if \_\_name\_\_ == '\_\_main\_\_':
    LineToDemo()
```
以上实例输出结果为：

![](https://www.runoob.com/wp-content/uploads/2015/10/tk7.jpg)

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)