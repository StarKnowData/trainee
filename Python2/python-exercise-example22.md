Python 练习实例22
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。

程序源代码：
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  for  i  in  range(ord('x'),ord('z') \+ 1): for  j  in  range(ord('x'),ord('z') \+ 1): if  i != j: for  k  in  range(ord('x'),ord('z') \+ 1): if  (i != k)  and  (j != k): if  (i != ord('x'))  and  (k != ord('x'))  and  (k != ord('z')): print  'order is a -- %s\\t b -- %s\\tc--%s' % (chr(i),chr(j),chr(k))
```
以上实例输出结果为：
```
order is a -- z     b -- x    c--y
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)