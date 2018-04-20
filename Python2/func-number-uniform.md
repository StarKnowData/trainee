Python uniform() 函数
===================

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

**uniform()** 方法将随机生成下一个实数，它在 \[x, y) 范围内。

* * *

语法
--

以下是 uniform() 方法的语法:
```
import random

random.uniform(x, y)
```
**注意：**uniform()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。

* * *

参数
--

*   x -- 随机数的最小值，包含该值。
*   y -- 随机数的最大值，不包含该值。

* * *

返回值
---

返回一个浮点数。

* * *

实例
--

以下展示了使用 uniform() 方法的实例：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import random

print "uniform(5, 10) 的随机数为 : ",  random.uniform(5, 10)

print "uniform(7, 14) 的随机数为 : ",  random.uniform(7, 14)
```
以上实例运行后输出结果为：
```
uniform(5, 10) 的随机数为 :  6.98774810047
uniform(7, 14) 的随机数为 :  12.2243345905
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)