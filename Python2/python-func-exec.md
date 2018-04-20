Python exec 内置语句
================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

exec 执行储存在字符串或文件中的Python语句，相比于 eval，exec可以执行更复杂的 Python 代码。

> 需要说明的是在 Python2 中exec不是函数，而是一个内置语句(statement)，但是Python 2中有一个 execfile() 函数。可以理解为 Python 3 把 exec 这个 statement 和 execfile() 函数的功能够整合到一个新的 exec() 函数中去了。

### 语法

以下是 exec 的语法:

exec obj

### 参数

*   obj -- 要执行的表达式。

### 返回值

exec 返回值永远为 None。

* * *

实例
--

以下展示了使用 exec 的实例：
```
实例 1
----

>>>exec  'print "Hello World"' 
Hello  World  
\# 单行语句字符串
>>> exec  "print 'runoob.com'"  runoob.com 
\# 多行语句字符串 
>>> exec  """for i in range(5): ... 
print "iter time: %d" % i ... """  iter  time: 0 
iter  time: 1  
iter  time: 2  
iter  time: 3  
iter  time: 4

实例 2
----

x = 10 
expr = """ 
z = 30 
sum = x + y + z 
print(sum) """  
def  func(): y = 20  exec(expr)  
exec(expr, {'x': 1, 'y': 2})
exec(expr, {'x': 1, 'y': 2},
{'y': 3, 'z': 4})  
func()
```
输出结果：
```
60
33
34
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)