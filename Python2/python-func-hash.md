Python hash() 函数
================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

**hash()** 用于获取取一个对象（字符串或者数值等）的哈希值。

语法
--

hash 语法：
```
hash(object)
```
参数说明：

*   object -- 对象；

返回值
---

返回对象的哈希值。

实例
--

以下实例展示了 hash 的使用方法：
```
>>>hash('test') 
\# 字符串  2314058222102390712 >>\> hash(1) 
\# 数字 
1 >>\> hash(str(\[1,2,3\])) 
\# 集合 1335416675971793195
>>\> hash(str(sorted({'1':1})))  
\# 字典  7666464346782421378 >>>
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)