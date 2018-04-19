Python index()方法
================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。

语法
--

index()方法语法：
```
str.index(str, beg=0, end=len(string))
```
参数
--

*   str -- 指定检索的字符串
*   beg -- 开始索引，默认为0。
*   end -- 结束索引，默认为字符串的长度。

返回值
---

如果包含子字符串返回开始的索引值，否则抛出异常。

实例
--

以下实例展示了index()方法的实例：
```
实例(Python 2.0+)
---------------

#!/usr/bin/python 

str1 = "this is string example....wow!!!";  
str2 = "exam"; print  str1.index(str2);   
print  str1.index(str2, 10);  
print  str1.index(str2, 40);
```
以上实例输出结果如下：
```
15
15
Traceback (most recent call last):
  File "test.py", line 8, in 
  print str1.index(str2, 40);
ValueError: substring not found

shell returned 1
```
### 注意: 
在接下来的几个章节中，我们会详细介绍Python Exception的使用。

* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)
