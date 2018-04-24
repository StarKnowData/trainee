Python 练习实例12
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**判断101-200之间有多少个素数，并输出所有素数。

**程序分析：**判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　　　　　

程序源代码：
```
实例(Python 2.0+)
---------------

#!/usr/bin/python 
\# -*- coding: UTF-8 -*-  

h = 0  leap = 1  from  math  import  sqrt  from  sys  import  stdout  for  m  in  range(101,201):
k = int(sqrt(m \+ 1))  for  i  in  range(2,k \+ 1): 
if  m % i == 0: leap = 0  break  
if  leap == 1: 
print  '%-4d' % m  h += 1  if  h % 10 == 0:
print  ''  leap = 1 
print  'The total is %d' % h
```
以上实例输出结果为：
```
101 
103 
107 
109 
113 
127 
131 
137 
139 
149 

151 
157 
163 
167 
173 
179 
181 
191 
193 
197 

199 
The total is 21
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)