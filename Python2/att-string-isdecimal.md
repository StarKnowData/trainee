Python isdecimal()方法
====================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python isdecimal() 方法检查字符串是否只包含十进制字符。这种方法只存在于unicode对象。

**注意:**定义一个十进制字符串，只需要在字符串前添加 'u' 前缀即可。

语法
--

isdecimal()方法语法：
```
str.isdecimal()
```
参数
--

*   无

返回值
---

如果字符串是否只包含十进制字符返回True，否则返回False。

实例
--

以下实例展示了 isdecimal()函数的使用方法：
```
#!/usr/bin/python str = u"this2009";  print str.isdecimal(); str = u"23443434";  print str.isdecimal();
```
以上实例输出结果如下：
```
False  True
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)
