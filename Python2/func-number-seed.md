Python seed() 函数
================

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

**seed()** 方法改变随机数生成器的种子，可以在调用其他随机模块函数之前调用此函数。。

* * *

语法
--

以下是 seed() 方法的语法:
```
import random

random.seed ( [x] )
```
**注意：**seed(()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。

* * *

参数
--

*   x -- 改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。

* * *

返回值
---

本函数没有返回值。

* * *

实例
--

以下展示了使用 seed(() 方法的实例：
```
#!/usr/bin/python
import random

random.seed( 10 )
print "Random number with seed 10 : ", random.random()

\# 生成同一个随机数
random.seed( 10 )
print "Random number with seed 10 : ", random.random()

\# 生成同一个随机数
random.seed( 10 )
print "Random number with seed 10 : ", random.random()
```
以上实例运行后输出结果为：
```
Random number with seed 10 :  0.57140259469
Random number with seed 10 :  0.57140259469
Random number with seed 10 :  0.57140259469
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)