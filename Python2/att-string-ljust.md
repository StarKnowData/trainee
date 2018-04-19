Python ljust()方法
================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。

语法
--

ljust()方法语法：
```
str.ljust(width[, fillchar])
```
参数
--

*   width -- 指定字符串长度。
*   fillchar -- 填充字符，默认为空格。

返回值
---

返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。

实例
--

以下实例展示了ljust()的使用方法：
```
#!/usr/bin/python

str = "this is string example....wow!!!";

print str.ljust(50, '0');
```
以上实例输出结果如下：
```
this is string example....wow!!!000000000000000000
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)
