Python globals() 函数
===================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

**globals()** 函数会以字典类型返回当前位置的全部全局变量。

语法
--

globals() 函数语法：
```
globals()
```
参数
--

*   无

返回值
---

返回全局变量的字典。

实例
--

以下实例展示了 globals() 的使用方法：
```
>>>a='runoob' 
>>\> print(globals()) 
\# globals 函数返回一个全局变量的字典，包括所有导入的变量。
{'\_\_builtins\_\_': <module  '\_\_builtin\_\_'  (built-in)>, '\_\_name\_\_': '\_\_main\_\_', '\_\_doc\_\_': None, 'a': 'runoob', '\_\_package\_\_': None}
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)