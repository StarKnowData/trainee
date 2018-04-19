Python partition() 方法
=====================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

partition() 方法用来根据指定的分隔符将字符串进行分割。

如果字符串包含指定的分隔符，则返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。

partition() 方法是在2.5版中新增的。

语法
--

partition()方法语法：
```
str.partition(str)
```
### 参数

str : 指定的分隔符。

返回值
---

返回一个3元的元组，第一个为分隔符左边的子串，第二个为分隔符本身，第三个为分隔符右边的子串。

实例
--

以下实例展示了使用 partition() 方法的使用：
```
#!/usr/bin/python

str = "http://www.w3cschool.cc/"

print str.partition("://")
```
输出结果为：
```
('http', '://', 'www.w3cschool.cc/')
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)
