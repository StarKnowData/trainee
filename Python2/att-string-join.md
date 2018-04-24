Python join()方法
===============

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。

语法
--

join()方法语法：
```
str.join(sequence)
```
参数
--

*   sequence -- 要连接的元素序列。

返回值
---

返回通过指定字符连接序列中元素后生成的新字符串。

实例
--

以下实例展示了join()的使用方法：
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  str = "-"; seq = ("a", "b", "c"); \# 字符串序列  print  str.join(  seq  );
```
以上实例输出结果如下：
```
a-b-c
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)
