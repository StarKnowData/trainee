Python endswith()方法
===================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python endswith() 方法用于判断字符串是否以指定后缀结尾，如果以指定后缀结尾返回True，否则返回False。可选参数"start"与"end"为检索字符串的开始与结束位置。

语法
--

endswith()方法语法：
```
str.endswith(suffix[, start[, end]])
```
参数
--

*   suffix -- 该参数可以是一个字符串或者是一个元素。
*   start -- 字符串中的开始位置。
*   end -- 字符中结束位置。

返回值
---

如果字符串含有指定的后缀返回True，否则返回False。

实例
--

以下实例展示了endswith()方法的实例：
```
#!/usr/bin/python

str = "this is string example....wow!!!";

suffix = "wow!!!";
print str.endswith(suffix);
print str.endswith(suffix,20);

suffix = "is";
print str.endswith(suffix, 2, 4);
print str.endswith(suffix, 2, 6);
```
以上实例输出结果如下：
```
True
True
True
False
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)
