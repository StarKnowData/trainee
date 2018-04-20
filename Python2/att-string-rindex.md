Python rindex()方法
=================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python rindex() 返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异常，你可以指定可选参数[beg:end]设置查找的区间。

语法
--

rindex()方法语法：
```
str.rindex(str, beg=0 end=len(string))
```
参数
--

*   str -- 查找的字符串
*   beg -- 开始查找的位置，默认为0
*   end -- 结束查找位置，默认为字符串的长度。

返回值
---

返回子字符串 str 在字符串中最后出现的位置，如果没有匹配的字符串会报异常。

实例
--

以下实例展示了rindex()函数的使用方法：
```
#!/usr/bin/python

str1 = "this is string example....wow!!!";
str2 = "is";

print str1.rindex(str2);
print str1.index(str2);
```
以上实例输出结果如下：
```
5
2
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)
