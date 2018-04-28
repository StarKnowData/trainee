Python next() 函数
================

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


  描述
--

 **next()** 返回迭代器的下一个项目。

 语法
--

 next 语法：

 
```

next(iterator[, default])

```

  参数说明：

  * iterator -- 可迭代对象
 * default -- 可选，用于设置在没有下一个元素时返回该默认值，如果不设置，又没有下一个元素则会触发 StopIteration 异常。
  返回值
---

 返回对象帮助信息。

 实例
--

 以下实例展示了 next 的使用方法：

  <pre>

#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
x = next(it)
print(x)
except StopIteration:
        # 遇到StopIteration就退出循环
break
</pre>

 输出结果为：

 
```

1
2
3
4
5

```

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


