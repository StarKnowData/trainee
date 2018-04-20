Python split()方法
================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python **split()** 通过指定分隔符对字符串进行切片，如果参数 num 有指定值，则仅分隔 num 个子字符串

语法
--

split() 方法语法：
```
str.split(str="", num=string.count(str)).
```
参数
--

*   str -- 分隔符，默认为所有的空字符，包括空格、换行(\\n)、制表符(\\t)等。
*   num -- 分割次数。

返回值
---

返回分割后的字符串列表。

实例
--

以下实例展示了split()函数的使用方法：
```
#!/usr/bin/python

str = "Line1-abcdef \nLine2-abc \nLine4-abcd";
print str.split( );
print str.split(' ', 1 );
```
以上实例输出结果如下：
```
['Line1-abcdef', 'Line2-abc', 'Line4-abcd']
['Line1-abcdef', '\nLine2-abc \nLine4-abcd']
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)