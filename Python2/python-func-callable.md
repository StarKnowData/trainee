Python callable() 函数
====================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

**callable()** 函数用于检查一个对象是否是可调用的。如果返回True，object仍然可能调用失败；但如果返回False，调用对象ojbect绝对不会成功。

对于函数, 方法, lambda 函式, 类, 以及实现了 \_\_call\_\_ 方法的类实例, 它都返回 True。

语法
--

callable()方法语法：
```
callable(object)
```
参数
--

*   object -- 对象

返回值
---

可调用返回 True，否则返回 False。

实例
--

以下实例展示了 callable() 的使用方法：
```
>>>callable(0)  False >>\> callable("runoob")  False >>\> def  add(a, b): ... return  a \+ b ... >>\> callable(add)  \# 函数返回 True  True >>\> class  A: \# 类 ... def  method(self): ... return  0 ... >>\> callable(A)  \# 类返回 True  True >>\> a = A() >>\> callable(a)  \# 没有实现 \_\_call\_\_, 返回 False  False >>\> class  B: ... def  \_\_call\_\_(self): ... return  0 ... >>\> callable(B)  True >>\> b = B() >>\> callable(b)  \# 实现 \_\_call\_\_, 返回 True  True
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)