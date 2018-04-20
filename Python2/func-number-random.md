Python random() 函数
==================

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

**random()** 方法返回随机生成的一个实数，它在\[0,1)范围内。

* * *

语法
--

以下是 random() 方法的语法:
```
import random

random.random()
```
**注意：**random()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。

* * *

参数
--

*   无

* * *

返回值
---

返回随机生成的一个实数，它在\[0,1)范围内。

* * *

实例
--

以下展示了使用 random() 方法的实例：
```
#!/usr/bin/python
import random

\# 生成第一个随机数
print "random() : ", random.random()

\# 生成第二个随机数
print "random() : ", random.random()
```
以上实例运行后输出结果为：
```
radom() :  0.281954791393
random() :  0.309090465205
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)