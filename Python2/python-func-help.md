Python help() 函数
================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

**help()** 函数用于查看函数或模块用途的详细说明。

语法
--

help 语法：
```
help(\[object\])
```
参数说明：

*   object -- 对象；

返回值
---

返回对象帮助信息。

实例
--

以下实例展示了 help 的使用方法：
```
>>>help('sys') 

\# 查看 sys 模块的帮助
……显示帮助信息……
>>>help('str') 

\# 查看 str 数据类型的帮助
……显示帮助信息…… >>>a = \[1,2,3\] >>>help(a)  
\# 查看列表 list 帮助信息
……显示帮助信息…… >>>help(a.append)  
\# 显示list的append方法的帮助
……显示帮助信息……
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)