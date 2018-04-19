Python islower()方法
==================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python islower() 方法检测字符串是否由小写字母组成。

语法
--

islower()方法语法：
```
str.islower()
```
参数
--

*   无。

返回值
---

如果字符串中包含至少一个区分大小写的字符，并且所有这些(区分大小写的)字符都是小写，则返回 True，否则返回 False

实例
--

以下实例展示了islower()方法的实例：
```
#!/usr/bin/python

str = "THIS is string example....wow!!!"; 
print str.islower();

str = "this is string example....wow!!!";
print str.islower();
```
以上实例输出结果如下：
```
False
True
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)
