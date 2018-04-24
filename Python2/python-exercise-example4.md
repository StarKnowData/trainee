Python 练习实例4
============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**输入某年某月某日，判断这一天是这一年的第几天？

**程序分析：**以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：

程序源代码：
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  
\# -*- coding: UTF-8 -*- 

year = int(raw_input('year:\\n')) 
month = int(raw_input('month:\\n'))

day = int(raw_input('day:\\n'))  

months = (0,31,59,90,120,151,181,212,243,273,304,334)
if  0 < month <= 12: 
sum = months\[month \- 1\] 
else: 
print  'data error' 
sum += day  leap = 0  
if  (year % 400 == 0)  or  ((year % 4 == 0)  and  (year % 100 != 0)): 
leap = 1  
if  (leap == 1)  and  (month \> 2):
sum += 1 
print  'it is the %dth day.' % sum
```
以上实例输出结果为：
```
year:  2015 month:  6 day:  7 it is the 158th day.
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)