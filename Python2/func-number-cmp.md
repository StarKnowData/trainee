Python cmp() 函数
===============

 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)

* * *

描述
--

cmp(x,y) 函数用于比较2个对象，如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。

* * *

语法
--

以下是 cmp() 方法的语法:
```
cmp( x, y )
```
* * *

参数
--

*   x -- 数值表达式。
*   y -- 数值表达式。

* * *

返回值
---

如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1。

* * *

实例
--

以下展示了使用 cmp() 方法的实例：
```
#!/usr/bin/python

print "cmp(80, 100) : ", cmp(80, 100)
print "cmp(180, 100) : ", cmp(180, 100)
print "cmp(-80, 100) : ", cmp(-80, 100)
print "cmp(80, -100) : ", cmp(80, -100)
```
以上实例运行后输出结果为：
```
cmp(80, 100) :  -1
cmp(180, 100) :  1
cmp(-80, 100) :  -1
cmp(80, -100) :  1
```
 [![Python 数字](../images/up.gif) Python 数字](python-numbers.html)