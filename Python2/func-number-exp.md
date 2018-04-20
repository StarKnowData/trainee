Python exp() 函数
===============

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

exp() 方法返回x的指数,ex。

* * *

语法
--

以下是 exp() 方法的语法:
```
import math

math.exp( x )
```
**注意：**exp()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。

* * *

参数
--

*   x -- 数值表达式。

* * *

返回值
---

返回x的指数,ex。

* * *

实例
--

以下展示了使用 exp() 方法的实例：
```
#!/usr/bin/python
import math   # 导入 math 模块

print "math.exp(-45.17) : ", math.exp(-45.17)
print "math.exp(100.12) : ", math.exp(100.12)
print "math.exp(100.72) : ", math.exp(100.72)
print "math.exp(119L) : ", math.exp(119L)
print "math.exp(math.pi) : ", math.exp(math.pi)
```
以上实例运行后输出结果为：
```
math.exp(-45.17) :  2.41500621326e-20
math.exp(100.12) :  3.03084361407e+43
math.exp(100.72) :  5.52255713025e+43
math.exp(119L) :  4.7978133273e+51
math.exp(math.pi) :  23.1406926328
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)