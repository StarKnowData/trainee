Python 字典 popitem() 方法
======================

 [![Python 字典](../images/up.gif) Python 字典](python-dictionary.html)

* * *

描述
--

Python 字典 popitem() 方法随机返回并删除字典中的一对键和值。

如果字典已经为空，却调用了此方法，就报出KeyError异常。

语法
--

popitem()方法语法：
```
popitem()
```
参数
--

*   无

返回值
---

返回一个键值对(key,value)形式。

实例
--

以下实例展示了 popitem() 方法的使用方法：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

site= {'name': '菜鸟教程', 'alexa': 10000, 'url': 'www.runoob.com'}
pop_obj=site.popitem()
print(pop_obj)
print(site)
```
输出结果为：
```
('url', 'www.runoob.com')
{'alexa': 10000, 'name': '\\xe8\\x8f\\x9c\\xe9\\xb8\\x9f\\xe6\\x95\\x99\\xe7\\xa8\\x8b'}
```
* * *

 [![Python 字典](../images/up.gif) Python 字典](python-dictionary.html)