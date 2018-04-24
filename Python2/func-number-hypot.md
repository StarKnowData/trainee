Python hypot() 函数
=================

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

**hypot()** 返回欧几里德范数 sqrt(x\*x + y\*y)。

* * *

语法
--

以下是 hypot() 方法的语法:
```
import math

math.hypot(x, y)
```
**注意：**hypot()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。

* * *

参数
--

*   x -- 一个数值。
*   y -- 一个数值。

* * *

返回值
---

返回欧几里德范数 sqrt(x\*x + y\*y)。

* * *

实例
--

以下展示了使用 hypot() 方法的实例：
```
#!/usr/bin/python
import math

print "hypot(3, 2) : ",  math.hypot(3, 2)
print "hypot(-3, 3) : ",  math.hypot(-3, 3)
print "hypot(0, 2) : ",  math.hypot(0, 2)
```
以上实例运行后输出结果为：
```
hypot(3, 2) :  3.60555127546
hypot(-3, 3) :  4.24264068712
hypot(0, 2) :  2.0
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)