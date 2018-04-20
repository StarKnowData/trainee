Python translate()方法
====================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python translate() 方法根据参数table给出的表(包含 256 个字符)转换字符串的字符, 要过滤掉的字符放到 del 参数中。

语法
--

translate()方法语法：
```
str.translate(table[, deletechars]);
```
参数
--

*   table -- 翻译表，翻译表是通过maketrans方法转换而来。
*   deletechars -- 字符串中要过滤的字符列表。

返回值
---

返回翻译后的字符串。

实例
--

以下实例展示了 translate()函数的使用方法：
```
#!/usr/bin/python

from string import maketrans   # 引用 maketrans 函数。

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!";
print str.translate(trantab);
```
以上实例输出结果如下：
```
th3s 3s str3ng 2x1mpl2....w4w!!!
```
以上实例去除字符串中的 'x' 和 'm' 字符：
```
#!/usr/bin/python

from string import maketrans   # Required to call maketrans function.

intab = "aeiou"
outtab = "12345"
trantab = maketrans(intab, outtab)

str = "this is string example....wow!!!";
print str.translate(trantab, 'xm');
```
以上实例输出结果：
```
th3s 3s str3ng 21pl2....w4w!!!
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)