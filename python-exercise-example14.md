Python 练习实例14
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**将一个正整数分解质因数。例如：输入90,打印出90=2\*3\*3*5。

**程序分析：**对n进行分解质因数，应先找到一个最小的质数k，然后按下述步骤完成：  
(1)如果这个质数恰等于n，则说明分解质因数的过程已经结束，打印出即可。  
(2)如果n<>k，但n能被k整除，则应打印出k的值，并用n除以k的商,作为新的正整数你n,重复执行第一步。  
(3)如果n不能被k整除，则用k+1作为k的值,重复执行第一步。

程序源代码：
```
实例(Python 2.0+)
---------------

#!/usr/bin/python 
\# -*- coding: UTF-8 -*-  
def  reduceNum(n): 
print  '{} = '.format(n), 
if  not  isinstance(n, int)  or  n <= 0 :
print  '请输入一个正确的数字 !'  
exit(0)

elif  n  in  \[1\] : 
print  '{}'.format(n)  
while  n  not  in  \[1\] : \# 循环保证递归  for  index  in  xrange(2, n \+ 1) : 
if  n % index == 0: n /= index  \# n 等于 n/index 
if  n == 1:
print  index 
else : \# index 一定是素数  
print  '{} *'.format(index), break  
reduceNum(90)  
reduceNum(100)
```
以上实例输出结果为：
```
90 =  2 * 3 * 3 * 5
100 =  2 * 2 * 5 * 5
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)