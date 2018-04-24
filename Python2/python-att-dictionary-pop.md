Python 字典 pop() 方法
==================

 [![Python 字典](../images/up.gif) Python 字典](python-dictionary.html)

* * *

描述
--

Python 字典 pop() 方法删除字典给定键 key 所对应的值，返回值为被删除的值。key值必须给出。 否则，返回default值。

语法
--

pop()方法语法：
```
pop(key[,default])
```
参数
--

*   key: 要删除的键值
*   default: 如果没有 key，返回 default 值

返回值
---

返回被删除的值。

实例
--

以下实例展示了 pop() 方法的使用方法：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.pop('name')
print pop_obj   // 输出 ：菜鸟教程
```
* * *

 [![Python 字典](../images/up.gif) Python 字典](python-dictionary.html)