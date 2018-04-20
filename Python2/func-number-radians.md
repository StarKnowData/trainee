Python radians() 函数
===================

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

**radians()** 方法将角度转换为弧度。

* * *

语法
--

以下是 radians() 方法的语法:
```
import math

math.radians(x)
```
**注意：**radians()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。

* * *

参数
--

*   x -- 一个数值。

* * *

返回值
---

返回一个角度的弧度值。

* * *

实例
--

以下展示了使用 radians() 方法的实例：
```
#!/usr/bin/python
import math

print "radians(3) : ",  math.radians(3)
print "radians(-3) : ",  math.radians(-3)
print "radians(0) : ",  math.radians(0)
print "radians(math.pi) : ",  math.radians(math.pi)
print "radians(math.pi/2) : ",  math.radians(math.pi/2)
print "radians(math.pi/4) : ",  math.radians(math.pi/4)
```
以上实例运行后输出结果为：
```
radians(3) :  0.0523598775598
radians(-3) :  -0.0523598775598
radians(0) :  0.0
radians(math.pi) :  0.0548311355616
radians(math.pi/2) :  0.0274155677808
radians(math.pi/4) :  0.0137077838904
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)