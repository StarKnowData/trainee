Python all() 函数
===============

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

all() 函数用于判断给定的可迭代参数 iterable 中的所有元素是否不为 0、''、False 或者 iterable 为空，如果是返回 True，否则返回 False。

函数等价于：

def all(iterable):  for element in iterable:  if  not element:  return  False  return  True

Python 2.5 以上版本可用。

### 语法

以下是 all() 方法的语法:

all(iterable)

### 参数

*   iterable -- 元组或列表。

### 返回值

如果iterable的所有元素不为0、''、False或者iterable为空，all(iterable)返回True，否则返回False；

**注意：**空元组、空列表返回值为True，这里要特别注意。

* * *

实例
--

以下展示了使用 all() 方法的实例：
```
>>>all(\['a', 'b', 'c', 'd'\])  \# 列表list，元素都不为空或0  True >>\> all(\['a', 'b', '', 'd'\])  \# 列表list，存在一个为空的元素  False >>\> all(\[0, 1，2, 3\])  \# 列表list，存在一个为0的元素  False >>\> all(('a', 'b', 'c', 'd'))  \# 元组tuple，元素都不为空或0  True >>\> all(('a', 'b', '', 'd'))  \# 元组tuple，存在一个为空的元素  False >>\> all((0, 1，2, 3))  \# 元组tuple，存在一个为0的元素  False >>\> all(\[\])  \# 空列表  True >>\> all(())  \# 空元组  True
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)