Python set() 函数
===============

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


  描述
--

 **set()** 函数创建一个无序不重复元素集，可进行关系测试，删除重复数据，还可以计算交集、差集、并集等。

 语法
--

 set 语法：

 
```

class set([iterable])

```

  参数说明：

  * iterable -- 可迭代对象对象；
  返回值
---

 返回新的集合对象。

 实例
--

 以下实例展示了 set 的使用方法：

  <pre>

>>>x = set('runoob')
>>> y = set('google')
>>> x, y
(set(['b', 'r', 'u', 'o', 'n']), set(['e', 'o', 'g', 'l'])) # 重复的被删除
>>> x & y # 交集
set(['o'])
>>> x | y # 并集
set(['b', 'e', 'g', 'l', 'o', 'n', 'r', 'u'])
>>> x - y # 差集
set(['r', 'b', 'u', 'n'])
>>>
</pre>

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


