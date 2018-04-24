Python sin() 函数
===============

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

**sin()** 返回的x弧度的正弦值。

* * *

语法
--

以下是 sin() 方法的语法:
```
import math

math.sin(x)
```
**注意：**sin()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。

* * *

参数
--

*   x -- 一个数值。

* * *

返回值
---

返回的x弧度的正弦值，数值在 -1 到 1 之间。

* * *

实例
--

以下展示了使用 sin() 方法的实例：
```
#!/usr/bin/python
import math

print "sin(3) : ",  math.sin(3)
print "sin(-3) : ",  math.sin(-3)
print "sin(0) : ",  math.sin(0)
print "sin(math.pi) : ",  math.sin(math.pi)
print "sin(math.pi/2) : ",  math.sin(math.pi/2)
```
以上实例运行后输出结果为：
```
sin(3) :  0.14112000806
sin(-3) :  -0.14112000806
sin(0) :  0.0
sin(math.pi) :  1.22460635382e-16
sin(math.pi/2) :  1
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)