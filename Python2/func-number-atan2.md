Python atan2() 函数
=================

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

**atan2()** 返回给定的 X 及 Y 坐标值的反正切值。

* * *

语法
--

以下是 atan2() 方法的语法:
```
import math

math.atan2(y, x)
```
**注意：**atan2()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。

* * *

参数
--

*   x -- 一个数值。
*   y -- 一个数值。

* * *

返回值
---

返回给定的 X 及 Y 坐标值的反正切值。

* * *

实例
--

以下展示了使用 atan2() 方法的实例：
```
#!/usr/bin/python
import math

print "atan2(-0.50,-0.50) : ",  math.atan2(-0.50,-0.50)
print "atan2(0.50,0.50) : ",  math.atan2(0.50,0.50)
print "atan2(5,5) : ",  math.atan2(5,5)
print "atan2(-10,10) : ",  math.atan2(-10,10)
print "atan2(10,20) : ",  math.atan2(10,20)
```
以上实例运行后输出结果为：
```
atan2(-0.50,-0.50) :  -2.35619449019
atan2(0.50,0.50) :  0.785398163397
atan2(5,5) :  0.785398163397
atan2(-10,10) :  -0.785398163397
atan2(10,20) :  0.463647609001
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)