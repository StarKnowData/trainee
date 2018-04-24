Python isnumeric()方法
====================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python isnumeric() 方法检测字符串是否只由数字组成。这种方法是只针对unicode对象。

**注：**定义一个字符串为Unicode，只需要在字符串前添加 'u' 前缀即可，具体可以查看本章节例子。

语法
--

isnumeric()方法语法：
```
str.isnumeric()
```
参数
--

*   无。

返回值
---

如果字符串中只包含数字字符，则返回 True，否则返回 False

实例
--

以下实例展示了isnumeric()方法的实例：
```
#!/usr/bin/python

str = u"this2009";  
print str.isnumeric();

str = u"23443434";
print str.isnumeric();
```
以上实例输出结果如下：
```
False
True
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)
