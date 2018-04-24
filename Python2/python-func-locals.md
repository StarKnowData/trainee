Python locals() 函数
==================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

**locals()** 函数会以字典类型返回当前位置的全部局部变量。

对于函数, 方法, lambda 函式, 类, 以及实现了 \_\_call\_\_ 方法的类实例, 它都返回 True。

语法
--

locals() 函数语法：
```
locals()
```
参数
--

*   无

返回值
---

返回字典类型的局部变量。

实例
--

以下实例展示了 locals() 的使用方法：
```
>>>def  runoob(arg): 

\# 两个局部变量：arg、z ... z = 1 ... print  (locals()) ...
>>\> runoob(4) {'z': 1, 'arg': 4} 
\# 返回一个名字/值对的字典
>>>
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)