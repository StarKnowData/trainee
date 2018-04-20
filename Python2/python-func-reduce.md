Python reduce() 函数
==================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

**reduce()** 函数会对参数序列中元素进行累积。

函数将一个数据集合（链表，元组等）中的所有数据进行下列操作：用传给reduce中的函数 function（有两个参数）先对集合中的第 1、2 个元素进行操作，得到的结果再与第三个数据用 function 函数运算，最后得到一个结果。

语法
--

reduce() 函数语法：
```
reduce(function, iterable\[, initializer\])
```
参数
--

*   function -- 函数，有两个参数
*   iterable -- 可迭代对象
*   initializer -- 可选，初始参数

返回值
---

返回函数计算结果。

实例
--

以下实例展示了 reduce() 的使用方法：
```
>>>def  add(x, y) :
\# 两数相加 ... return  x \+ y ... 
>>\> reduce(add, \[1,2,3,4,5\]) 
\# 计算列表和：1+2+3+4+5  15
>>\> reduce(lambda  x, y: x+y, \[1,2,3,4,5\])  
\# 使用 lambda 匿名函数  15
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)