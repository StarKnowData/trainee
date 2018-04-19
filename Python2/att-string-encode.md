Python encode()方法
=================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python encode() 方法以 _encoding_ 指定的编码格式编码字符串。errors参数可以指定不同的错误处理方案。

语法
--

encode()方法语法：
```
str.encode(encoding='UTF-8',errors='strict')
```
参数
--

*   encoding -- 要使用的编码，如"UTF-8"。
*   errors -- 设置不同错误的处理方案。默认为 'strict',意为编码错误引起一个UnicodeError。 其他可能得值有 'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 以及通过 codecs.register_error() 注册的任何值。

返回值
---

该方法返回编码后的字符串。

实例
--

以下实例展示了encode()方法的实例：
```
#!/usr/bin/python

str = "this is string example....wow!!!";

print "Encoded String: " + str.encode('base64','strict')
```
以上实例输出结果如下：
```
Encoded String: dGhpcyBpcyBzdHJpbmcgZXhhbXBsZS4uLi53b3chISE=
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)
