Python isupper()方法
==================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python isupper() 方法检测字符串中所有的字母是否都为大写。

语法
--

isupper()方法语法：
```
str.isupper()
```
参数
--

*   无。

返回值
---

如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是大写，则返回 True，否则返回 False

实例
--

以下实例展示了isupper()方法的实例：
```
#!/usr/bin/python

str = "THIS IS STRING EXAMPLE....WOW!!!"; 
print str.isupper();

str = "THIS is string example....wow!!!";
print str.isupper();
```
以上实例输出结果如下：
```
True
False
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)
