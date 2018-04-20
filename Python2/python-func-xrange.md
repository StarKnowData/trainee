Python xrange() 函数
==================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

**xrange()** 函数用法与 [range](python-func-range.html) 完全相同，所不同的是生成的不是一个数组，而是一个生成器。

语法
--

xrange 语法：
```
xrange(stop)
xrange(start, stop\[, step\])
```
参数说明：

*   start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
*   stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是\[0, 1, 2, 3, 4\]没有5
*   step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)

返回值
---

返回生成器。

实例
--

以下实例展示了 xrange 的使用方法：
```
>>>xrange(8)  xrange(8) 
>>\> list(xrange(8))  \[0, 1, 2, 3, 4, 5, 6, 7\] 
>>\> range(8)  
\# range 使用  \[0, 1, 2, 3, 4, 5, 6, 7\] 
>>\> xrange(3, 5)  xrange(3, 5) 
>>\> list(xrange(3,5))  \[3, 4\] >>\> range(3,5) 
\# 使用 range  \[3, 4\] 
>>\> xrange(0,6,2)  
xrange(0, 6, 2)  
\# 步长为 2
>>\> list(xrange(0,6,2))  
\[0, 2, 4\] >>>
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)