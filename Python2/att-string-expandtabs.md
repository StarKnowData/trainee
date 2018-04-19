Python expandtabs()方法
=====================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python expandtabs() 方法把字符串中的 tab 符号('\\t')转为空格，tab 符号('\\t')默认的空格数是 8。

语法
--

expandtabs()方法语法：
```
str.expandtabs(tabsize=8)
```
参数
--

*   tabsize -- 指定转换字符串中的 tab 符号('\\t')转为空格的字符数。

返回值
---

该方法返回字符串中的 tab 符号('\\t')转为空格后生成的新字符串。

实例
--

以下实例展示了expandtabs()方法的实例：
```
#!/usr/bin/python

str = "this is\\tstring example....wow!!!";


print "Original string: " + str;
print "Defualt exapanded tab: " +  str.expandtabs();
print "Double exapanded tab: " +  str.expandtabs(16);
```
以上实例输出结果如下：
```
Original string: this is        string example....wow!!!
Defualt exapanded tab: this is string example....wow!!!
Double exapanded tab: this is         string example....wow!!!
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)
