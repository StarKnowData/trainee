Python fabs() 函数
================

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

fabs() 方法返回数字的绝对值，如math.fabs(-10) 返回10.0。

* * *

语法
--

以下是 fabs() 方法的语法:
```
import math

math.fabs( x )
```
**注意：**fabs()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。

* * *

参数
--

*   x -- 数值表达式。

* * *

返回值
---

返回数字的绝对值。

* * *

实例
--

以下展示了使用 fabs() 方法的实例：
````
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import math   # 导入数学模块

print "math.fabs(-45.17) : ", math.fabs(-45.17)
print "math.fabs(100.12) : ", math.fabs(100.12)
print "math.fabs(100.72) : ", math.fabs(100.72)
print "math.fabs(119L) : ", math.fabs(119L)
print "math.fabs(math.pi) : ", math.fabs(math.pi)
````
以上实例运行后输出结果为：
```
math.fabs(-45.17) :  45.17
math.fabs(100.12) :  100.12
math.fabs(100.72) :  100.72
math.fabs(119L) :  119.0
math.fabs(math.pi) :  3.14159265359
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)