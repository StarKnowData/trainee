Python isalpha()方法
==================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python isalpha() 方法检测字符串是否只由字母组成。

语法
--

isalpha()方法语法：
```
str.isalpha()
```
参数
--

*   无。

返回值
---

如果字符串至少有一个字符并且所有字符都是字母则返回 True,否则返回 False

实例
--

以下实例展示了isalpha()方法的实例：
```
#!/usr/bin/python

str = "this";   
# No space & digit in this string
print str.isalpha();

str = "this is string example....wow!!!";
print str.isalpha();
```
以上实例输出结果如下：
```
True
False
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)
