Python rjust()方法
================

* * *

描述
--

Python rjust() 返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串。

语法
--

rjust()方法语法：
```
str.rjust(width[, fillchar])
```
参数
--

*   width -- 指定填充指定字符后中字符串的总长度.
*   fillchar -- 填充的字符，默认为空格。

返回值
---

返回一个原字符串右对齐,并使用空格填充至长度 width 的新字符串。如果指定的长度小于字符串的长度则返回原字符串

实例
--

以下实例展示了rjust()函数的使用方法：
```
#!/usr/bin/python

str = "this is string example....wow!!!";

print str.rjust(50, '0');
```
以上实例输出结果如下：
```
000000000000000000this is string example....wow!!!
```