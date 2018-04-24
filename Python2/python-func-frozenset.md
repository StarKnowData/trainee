Python frozenset() 函数
=====================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

**frozenset()** 返回一个冻结的集合，冻结后集合不能再添加或删除任何元素。

语法
--

frozenset() 函数语法：
```
class frozenset([iterable])
```
参数
--

*   iterable -- 可迭代的对象，比如列表、字典、元组等等。

返回值
---

返回新的 frozenset 对象，如果不提供任何参数，默认会生成空集合。

实例
--

以下实例展示了 frozenset() 的使用方法：
```
>>>a = frozenset(range(10)) 
\# 生成一个新的不可变集合
>>> a  frozenset([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> b = frozenset('runoob')
>>> b  frozenset(['b', 'r', 'u', 'o', 'n'])  
\# 创建不可变集合 
>>>
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)