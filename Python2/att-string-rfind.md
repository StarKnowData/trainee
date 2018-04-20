Python rfind()方法
================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python rfind() 返回字符串最后一次出现的位置(从右向左查询)，如果没有匹配项则返回-1。

语法
--

rfind()方法语法：
```
str.rfind(str, beg=0 end=len(string))
```
参数
--

*   str -- 查找的字符串
*   beg -- 开始查找的位置，默认为 0
*   end -- 结束查找位置，默认为字符串的长度。

返回值
---

返回字符串最后一次出现的位置，如果没有匹配项则返回-1。

实例
--

以下实例展示了rfind()函数的使用方法：
```
#!/usr/bin/python

str = "this is really a string example....wow!!!";
substr = "is";

print str.rfind(substr);
print str.rfind(substr, 0, 10);
print str.rfind(substr, 10, 0);

print str.find(substr);
print str.find(substr, 0, 10);
print str.find(substr, 10, 0);
```
以上实例输出结果如下：
```
5
5
-1
2
2
-1
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)