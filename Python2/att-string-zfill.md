Python zfill()方法
================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python zfill() 方法返回指定长度的字符串，原字符串右对齐，前面填充0。

语法
--

zfill()方法语法：
```
str.zfill(width)
```
参数
--

*   width -- 指定字符串的长度。原字符串右对齐，前面填充0。

返回值
---

返回指定长度的字符串。

实例
--

以下实例展示了 zfill()函数的使用方法：
```
#!/usr/bin/python

str = "this is string example....wow!!!";

print str.zfill(40);
print str.zfill(50);
```
以上实例输出结果如下：
```
00000000this is string example....wow!!!
000000000000000000this is string example....wow!!!
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)
