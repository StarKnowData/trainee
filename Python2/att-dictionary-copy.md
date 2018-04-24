Python List pop()方法
===================

 [![Python 列表](../images/up.gif) Python 列表](python-lists.html)

* * *

描述
--

pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值。

语法
--

pop()方法语法：
```
list.pop(obj=list[-1])
```
参数
--

*   obj -- 可选参数，要移除列表元素的对象。

返回值
---

该方法返回从列表中移除的元素对象。

实例
--

以下实例展示了 pop()函数的使用方法：
```
#!/usr/bin/python3
#coding=utf-8

list1 = ['Google', 'Runoob', 'Taobao']
list_pop=list1.pop(1)
print "删除的项为 :", list_pop
print "列表现在为 : ", list1
```
以上实例输出结果如下：
```
删除的项为 : Runoob
列表现在为 : ['Google', 'Taobao']
```
 [![Python 列表](../images/up.gif) Python 列表](python-lists.html)
