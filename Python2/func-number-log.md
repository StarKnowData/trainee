Python log() 函数
===============

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

log() 方法返回x的自然对数。

* * *

语法
--

以下是 log() 方法的语法:
```
import math

math.log( x )
```
**注意：**log()是不能直接访问的，需要导入 math 模块，通过静态对象调用该方法。

* * *

参数
--

*   x -- 数值表达式。

* * *

返回值
---

返回x的自然对数，x>0。

* * *

实例
--

以下展示了使用 log() 方法的实例：
```
#!/usr/bin/python   
import math \# This will import math module    
print  "math.log(100.12) : ", math.log(100.12)   
print  "math.log(100.72) : ", math.log(100.72)   
print  "math.log(119L) : ", math.log(119L)  
print  "math.log(math.pi) : ", math.log(math.pi)
```
以上实例运行后输出结果为：

math.log(100.12)  :  4.60636946656 math.log(100.72)  :  4.61234438974 math.log(119L)  :  4.77912349311 math.log(math.pi)  :  1.14472988585

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)