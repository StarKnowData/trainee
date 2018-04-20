Python setattr() 函数
===================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

**setattr** 函数对应函数 [getatt()](python-func-getattr.html)，用于设置属性值，该属性必须存在。

语法
--

setattr 语法：
```
setattr(object, name, value)
```
参数
--

*   object -- 对象。
*   name -- 字符串，对象属性。
*   value -- 属性值。

返回值
---

无。

实例
--

以下实例展示了 setattr 的使用方法：
```
>>>class  A(object): 
... bar = 1 ... 
>>\> a = A() 
>>\> getattr(a, 'bar')  
\# 获取属性 bar 值  1 
>>\> setattr(a, 'bar', 5)  
\# 设置属性 bar 值 
>>\> a.bar  5
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)