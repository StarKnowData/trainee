Python atan() 函数
================

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

**atan()** 返回x的反正切弧度值。

* * *

语法
--

以下是 atan() 方法的语法:
```
import math

math.atan(x)
```
**注意：**atan()是不能直接访问的，需要导入 math 模块，然后通过 math 静态对象调用该方法。

* * *

参数
--

*   x -- 一个数值。

* * *

返回值
---

返回x的反正切弧度值。

* * *

实例
--

以下展示了使用 atan() 方法的实例：
```
#!/usr/bin/python   

import math   
print  "atan(0.64) : ",  math.atan(0.64)   
print  "atan(0) : ", math.atan(0) 
print  "atan(10) : ", math.atan(10)
print  "atan(-1) : ", math.atan(-1)
print  "atan(1) : ", math.atan(1)
```
以上实例运行后输出结果为：
```
atan(0.64)  :  0.569313191101
atan(0)  :  0.0
atan(10) :  1.4711276743
atan(-1)  :  -0.785398163397 
atan(1)  :  0.785398163397
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)