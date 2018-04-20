Python sqrt() 函数
================

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

**sqrt()** 方法返回数字x的平方根。

* * *

语法
--

以下是 sqrt() 方法的语法:
```
import math

math.sqrt( x )
```
**注意：**sqrt()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。

* * *

参数
--

*   x -- 数值表达式。

* * *

返回值
---

返回数字x的平方根。

* * *

实例
--

以下展示了使用 sqrt() 方法的实例：
```
#!/usr/bin/python
import math   # This will import math module

print "math.sqrt(100) : ", math.sqrt(100)
print "math.sqrt(7) : ", math.sqrt(7)
print "math.sqrt(math.pi) : ", math.sqrt(math.pi)
```
以上实例运行后输出结果为：
```
math.sqrt(100) :  10.0
math.sqrt(7) :  2.64575131106
math.sqrt(math.pi) :  1.77245385091
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)