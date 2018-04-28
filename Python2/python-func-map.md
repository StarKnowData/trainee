Python map() 函数
===============

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


  描述
--

 **map()** 会根据提供的函数对指定序列做映射。

 第一个参数 function 以参数序列中的每一个元素调用 function 函数，返回包含每次 function 函数返回值的新列表。

 语法
--

 map() 函数语法：

 
```

map(function, iterable, ...)

```

 参数
--

  * function -- 函数，有两个参数
 * iterable -- 一个或多个序列
  返回值
---

 Python 2.x 返回列表。

 Python 3.x 返回迭代器。

 实例
--

 以下实例展示了 map() 的使用方法：

  <pre>

>>>def square(x) :            # 计算平方数
...     return x ** 2
... 
>>> map(square, [1,2,3,4,5]) # 计算列表各个元素的平方
[1, 4, 9, 16, 25]
>>> map(lambda x: x ** 2, [1, 2, 3, 4, 5]) # 使用 lambda 匿名函数
[1, 4, 9, 16, 25]
# 提供了两个列表，对相同位置的列表数据进行相加
>>> map(lambda x, y: x + y, [1, 3, 5, 7, 9], [2, 4, 6, 8, 10])
[3, 7, 11, 15, 19]
</pre>

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)
