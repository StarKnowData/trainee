Python 练习实例6
============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**斐波那契数列。

**程序分析：**斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

在数学上，费波那契数列是以递归的方法来定义：
```
F0 = 0     (n=0)
F1 = 1    (n=1)
Fn = F\[n-1\]+ F\[n-2\](n=>2)
```
程序源代码：

方法一
---
```
#!/usr/bin/python  
\# -*- coding: UTF-8 -*- 
def  fib(n): a,b = 1,1
for  i  in  range(n-1): a,b = b,a+b  
return  a 
\# 输出了第10个斐波那契数列 
print  fib(10)
```
方法二
---
```
#!/usr/bin/python 
\# -*- coding: UTF-8 -*- 
\# 使用递归 
def  fib(n): 
if  n==1  or  n==2: 
return  1 
return  fib(n-1)+fib(n-2) 
\# 输出了第10个斐波那契数列
print  fib(10)
```
以上实例输出了第10个斐波那契数列，结果为：

55

方法三
---

如果你需要输出指定个数的斐波那契数列，可以使用以下代码：
```
#!/usr/bin/python 
\# -*- coding: UTF-8 -*- 
def  fib(n): 
if  n == 1: return  \[1\]  
if  n == 2: return  \[1, 1\]
fibs = \[1, 1\]  
for  i  in  range(2, n):
fibs.append(fibs\[-1\] \+ fibs\[-2\])  
return  fibs  
\# 输出前 10 个斐波那契数列 
print  fib(10)
```
以上程序运行输出结果为：
```
\[1, 1, 2, 3, 5, 8, 13, 21, 34, 55\]
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)