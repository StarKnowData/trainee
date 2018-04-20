Python eval() 函数
================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

eval() 函数用来执行一个字符串表达式，并返回表达式的值。

### 语法

以下是 eval() 方法的语法:
```
eval(expression[, globals[, locals]])
```
### 参数

*   expression -- 表达式。
*   globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
*   locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。

### 返回值

返回表达式计算结果。

* * *

实例
--

以下展示了使用 eval() 方法的实例：
```
>>>x = 7
>>> eval(  '3 * x'  )  21 
>>> eval('pow(2,2)')  4 
>>> eval('2 + 2')  4 
>>> n=81
>>> eval("n + 4")  85
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)