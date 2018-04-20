Python degrees() 函数
===================

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

**degrees()** 将弧度转换为角度。

* * *

语法
--

以下是 degrees() 方法的语法:
```
import math

math.degrees(x)
```
**注意：**degrees()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。

* * *

参数
--

*   x -- 一个数值。

* * *

返回值
---

返回一个角度值。

* * *

实例
--

以下展示了使用 degrees() 方法的实例：
```
#!/usr/bin/python
import math

print "degrees(3) : ",  math.degrees(3)
print "degrees(-3) : ",  math.degrees(-3)
print "degrees(0) : ",  math.degrees(0)
print "degrees(math.pi) : ",  math.degrees(math.pi)
print "degrees(math.pi/2) : ",  math.degrees(math.pi/2)
print "degrees(math.pi/4) : ",  math.degrees(math.pi/4)
```
以上实例运行后输出结果为：
```
degrees(3) :  171.887338539
degrees(-3) :  -171.887338539
degrees(0) :  0.0
degrees(math.pi) :  180.0
degrees(math.pi/2) :  90.0
degrees(math.pi/4) :  45.0
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)