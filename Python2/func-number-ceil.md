Python ceil() 函数
================

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

ceil() 函数返回数字的上入整数。

* * *

语法
--

以下是 ceil() 方法的语法:
```
import math

math.ceil( x )
```
**注意：**ceil()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。

* * *

参数
--

x -- 数值表达式。

* * *

返回值
---

函数返回数字的上入整数。

* * *

实例
--

以下展示了使用 ceil() 方法的实例：
```
#!/usr/bin/python
import math   # This will import math module

print "math.ceil(-45.17) : ", math.ceil(-45.17)
print "math.ceil(100.12) : ", math.ceil(100.12)
print "math.ceil(100.72) : ", math.ceil(100.72)
print "math.ceil(119L) : ", math.ceil(119L)
print "math.ceil(math.pi) : ", math.ceil(math.pi)
```
以上实例运行后输出结果为：
```
math.ceil(-45.17) :  -45.0
math.ceil(100.12) :  101.0
math.ceil(100.72) :  101.0
math.ceil(119L) :  119.0
math.ceil(math.pi) : 4.0
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)