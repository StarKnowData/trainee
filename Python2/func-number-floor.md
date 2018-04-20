Python floor() 函数
=================

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

floor() 返回数字的下舍整数。

* * *

语法
--

以下是 floor() 方法的语法:
```
import math

math.floor( x )
```
**注意：**floor()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。

* * *

参数
--

*   x -- 数值表达式。

* * *

返回值
---

返回数字的下舍整数。

* * *

实例
--

以下展示了使用 floor() 方法的实例：
```
#!/usr/bin/python
import math   # This will import math module

print "math.floor(-45.17) : ", math.floor(-45.17)
print "math.floor(100.12) : ", math.floor(100.12)
print "math.floor(100.72) : ", math.floor(100.72)
print "math.floor(119L) : ", math.floor(119L)
print "math.floor(math.pi) : ", math.floor(math.pi)
```
以上实例运行后输出结果为：
```
math.floor(-45.17) :  -46.0
math.floor(100.12) :  100.0
math.floor(100.72) :  100.0
math.floor(119L) :  119.0
math.floor(math.pi) :  3.0
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)