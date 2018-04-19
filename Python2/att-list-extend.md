Python List extend()方法
======================

 [![Python 列表](../images/up.gif) Python 列表](python-lists.html)

* * *

描述
--

extend() 函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。

语法
--

extend()方法语法：
```
list.extend(seq)
```
参数
--

*   seq -- 元素列表。

返回值
---

该方法没有返回值，但会在已存在的列表中添加新的列表内容。

实例
--

以下实例展示了 extend()函数的使用方法：
```
#!/usr/bin/python

aList = [123, 'xyz', 'zara', 'abc', 123];
bList = [2009, 'manni'];
aList.extend(bList)

print "Extended List : ", aList ;
````
以上实例输出结果如下：
```
Extended List :  [123, 'xyz', 'zara', 'abc', 123, 2009, 'manni']
```
 [![Python 列表](../images/up.gif) Python 列表](python-lists.html)
