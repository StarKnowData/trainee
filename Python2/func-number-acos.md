Python acos() 函数
================

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

**acos()** 返回x的反余弦弧度值。

* * *

语法
--

以下是 acos() 方法的语法:
```
import math

math.acos(x)
```
**注意：**acos()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。

* * *

参数
--

*   x -- -1到1之间的数值。如果x是大于1，会产生一个错误。

* * *

返回值
---

返回x的反余弦弧度值。

* * *

实例
--

以下展示了使用 acos() 方法的实例：
```
#!/usr/bin/python
import math

print "acos(0.64) : ",  math.acos(0.64)
print "acos(0) : ",  math.acos(0)
print "acos(-1) : ",  math.acos(-1)
print "acos(1) : ",  math.acos(1)
```
以上实例运行后输出结果为：
```
acos(0.64) :  0.876298061168
acos(0) :  1.57079632679
acos(-1) :  3.14159265359
acos(1) :  0.0
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)