Python List remove()方法
======================

 [![Python 列表](../images/up.gif) Python 列表](python-lists.html)

* * *

描述
--

remove() 函数用于移除列表中某个值的第一个匹配项。

语法
--

remove()方法语法：
```
list.remove(obj)
```
参数
--

*   obj -- 列表中要移除的对象。

返回值
---

该方法没有返回值但是会移除列表中的某个值的第一个匹配项。

实例
--

以下实例展示了 remove()函数的使用方法：
```
#!/usr/bin/python

aList = [123, 'xyz', 'zara', 'abc', 'xyz'];

aList.remove('xyz');
print "List : ", aList;
aList.remove('abc');
print "List : ", aList;
```
以上实例输出结果如下：
```
List :  [123, 'zara', 'abc', 'xyz']
List :  [123, 'zara', 'xyz']
```
 [![Python 列表](../images/up.gif) Python 列表](python-lists.html)
