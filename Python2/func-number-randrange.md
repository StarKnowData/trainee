Python randrange() 函数
=====================

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

**randrange()** 方法返回指定递增基数集合中的一个随机数，基数缺省值为1。

* * *

语法
--

以下是 randrange() 方法的语法:
```
import random

random.randrange ([start,] stop [,step])
```
**注意：**randrange()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。

* * *

参数
--

*   start -- 指定范围内的开始值，包含在范围内。
*   stop -- 指定范围内的结束值，不包含在范围内。
*   step -- 指定递增基数。

* * *

返回值
---

从给定的范围返回随机项。

* * *

实例
--

以下展示了使用 randrange() 方法的实例：
```
#!/usr/bin/python
import random

\# 输出 100 <= number < 1000 间的偶数
print "randrange(100, 1000, 2) : ", random.randrange(100, 1000, 2)

\# 输出 100 <= number < 1000 间的其他数
print "randrange(100, 1000, 3) : ", random.randrange(100, 1000, 3)
```
以上实例运行后输出结果为：
```
randrange(100, 1000, 2) :  976
randrange(100, 1000, 3) :  520
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)