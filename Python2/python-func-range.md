Python range() 函数用法
===================

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


 python range() 函数可创建一个整数列表，一般用在 for 循环中。

 ### 函数语法

 
```

range(start, stop[, step])

```

  参数说明：

 * start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
 * stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
 * step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)
 ### 实例

  <pre>

>>>range(10) # 从 0 开始到 10
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> range(1, 11) # 从 1 开始到 11
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> range(0, 30, 5) # 步长为 5
[0, 5, 10, 15, 20, 25]
>>> range(0, 10, 3) # 步长为 3
[0, 3, 6, 9]
>>> range(0, -10, -1) # 负数
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
>>> range(0)
[]
>>> range(1, 0)
[]
</pre>

 以下是 range 在 for 中的使用，循环出runoob 的每个字母:

  <pre>

>>>x = 'runoob'
>>> for i in range(len(x)) :
...     print(x[i])
... 
r
u
n
o
o
b
>>>
</pre>

[![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


