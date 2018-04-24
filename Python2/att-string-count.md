Python count()方法
================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python count() 方法用于统计字符串里某个字符出现的次数。可选参数为在字符串搜索的开始与结束位置。

语法
--

count()方法语法：
```
str.count(sub, start= 0,end=len(string))
```
参数
--

*   sub -- 搜索的子字符串
*   start -- 字符串开始搜索的位置。默认为第一个字符,第一个字符索引值为0。
*   end -- 字符串中结束搜索的位置。字符中第一个字符的索引为 0。默认为字符串的最后一个位置。

返回值
---

该方法返回子字符串在字符串中出现的次数。

实例
--

以下实例展示了count()方法的实例：

实例(Python 2.0+)
---------------
```
#!/usr/bin/python 

str = "this is string example....wow!!!";   

sub = "i";   
print  "str.count(sub, 4, 40) : ", str.count(sub, 4, 40)   
sub = "wow";   
print  "str.count(sub) : ", str.count(sub)
```
以上实例输出结果如下：
```
str.count(sub, 4, 40) :  2
str.count(sub) :  1
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)
