Python List insert()方法
======================

 [![Python 列表](../images/up.gif) Python 列表](python-lists.html)

* * *

描述
--

insert() 函数用于将指定对象插入列表的指定位置。

语法
--

insert()方法语法：
```
list.insert(index, obj)
```
参数
--

*   index -- 对象 obj 需要插入的索引位置。
*   obj -- 要插入列表中的对象。

返回值
---

该方法没有返回值，但会在列表指定位置插入对象。

实例
--

以下实例展示了 insert()函数的使用方法：
```
#!/usr/bin/python

aList = [123, 'xyz', 'zara', 'abc']

aList.insert( 3, 2009)

print "Final List : ", aList
```
以上实例输出结果如下：
```
Final List : [123, 'xyz', 'zara', 2009, 'abc']
```
 [![Python 列表](../images/up.gif) Python 列表](python-lists.html)
