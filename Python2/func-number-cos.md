Python cos() 函数
===============

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

**cos()** 返回x的弧度的余弦值。

* * *

语法
--

以下是 cos() 方法的语法:
```
import math

math.cos(x)
```
**注意：**cos()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。

* * *

参数
--

*   x -- 一个数值。

* * *

返回值
---

返回x的弧度的余弦值,-1 到 1 之间。

* * *

实例
--

以下展示了使用 cos() 方法的实例：
```
#!/usr/bin/python
import math

print "cos(3) : ",  math.cos(3)
print "cos(-3) : ",  math.cos(-3)
print "cos(0) : ",  math.cos(0)
print "cos(math.pi) : ",  math.cos(math.pi)
print "cos(2\*math.pi) : ",  math.cos(2\*math.pi)
```
以上实例运行后输出结果为：
```
cos(3) :  -0.9899924966
cos(-3) :  -0.9899924966
cos(0) :  1.0
cos(math.pi) :  -1.0
cos(2*math.pi) :  1.0
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)