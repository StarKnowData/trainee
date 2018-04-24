Python rstrip()方法
=================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python rstrip() 删除 string 字符串末尾的指定字符（默认为空格）.

语法
--

rstrip()方法语法：
```
str.rstrip([chars])
```
参数
--

*   chars -- 指定删除的字符（默认为空格）

返回值
---

返回删除 string 字符串末尾的指定字符后生成的新字符串。

实例
--

以下实例展示了rstrip()函数的使用方法：
```
#!/usr/bin/python  
str =  "     this is string example....wow!!!     ";   
print str.rstrip(); str =  "88888888this is string example....wow!!!8888888";   
print str.rstrip('8');
```
以上实例输出结果如下：
```
  this  is  string example....wow!!!  88888888this  is  string example....wow!!!
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)