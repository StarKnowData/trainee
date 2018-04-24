Python List sort()方法
====================

 [![Python 列表](../images/up.gif) Python 列表](python-lists.html)

* * *

描述
--

sort() 函数用于对原列表进行排序，如果指定参数，则使用比较函数指定的比较函数。

语法
--

sort()方法语法：
```
list.sort([func])
```
参数
--

*   func -- 可选参数, 如果指定了该参数会使用该参数的方法进行排序。

返回值
---

该方法没有返回值，但是会对列表的对象进行排序。

实例
--

以下实例展示了 sort()函数的使用方法：
```
#!/usr/bin/python

aList = [123, 'xyz', 'zara', 'abc', 'xyz'];

aList.sort();
print "List : ", aList;
```
以上实例输出结果如下：
```
List :  [123, 'abc', 'xyz', 'xyz', 'zara']
```
 [![Python 列表](../images/up.gif) Python 列表](python-lists.html)
