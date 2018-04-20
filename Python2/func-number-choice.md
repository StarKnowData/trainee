Python choice() 函数
==================

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

**choice()** 方法返回一个列表，元组或字符串的随机项。

* * *

语法
--

以下是 choice() 方法的语法:
```
import random

random.choice( seq  )
```
**注意：**choice()是不能直接访问的，需要导入 random 模块，然后通过 random 静态对象调用该方法。

* * *

参数
--

*   seq -- 可以是一个列表，元组或字符串。

* * *

返回值
---

返回随机项。

* * *

实例
--

以下展示了使用 choice() 方法的实例：
```
#!/usr/bin/python
import random

print "choice([1, 2, 3, 5, 9]) : ", random.choice([1, 2, 3, 5, 9])
print "choice('A String') : ", random.choice('A String')
```
以上实例运行后输出结果为：
```
choice([1, 2, 3, 5, 9]) :  2
choice('A String') :  n
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)