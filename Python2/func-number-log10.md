Python log10() 函数
=================

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

log10() 方法返回以10为基数的x对数。

* * *

语法
--

以下是 log10() 方法的语法:
```
import math

math.log10( x )
```
**注意：**log10()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。

* * *

参数
--

*   x -- 数值表达式。

* * *

返回值
---

返回以10为基数的x对数，x>0。

* * *

实例
--

以下展示了使用 log10() 方法的实例：
```
#!/usr/bin/python
import math   # 导入 math 模块

print "math.log10(100.12) : ", math.log10(100.12)
print "math.log10(100.72) : ", math.log10(100.72)
print "math.log10(119L) : ", math.log10(119L)
print "math.log10(math.pi) : ", math.log10(math.pi)
```
以上实例运行后输出结果为：
```
math.log10(100.12) :  2.00052084094
math.log10(100.72) :  2.0031157171
math.log10(119L) :  2.07554696139
math.log10(math.pi) :  0.497149872694
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)