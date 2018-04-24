Python strip()方法
================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python strip() 方法用于移除字符串头尾指定的字符（默认为空格）。

语法
--

strip()方法语法：
```
str.strip([chars]);
```
参数
--

*   chars -- 移除字符串头尾指定的字符。

返回值
---

返回移除字符串头尾指定的字符生成的新字符串。

实例
--

以下实例展示了strip()函数的使用方法：
```
实例(Python 2.0+)
---------------

#!/usr/bin/python    
\# -*- coding: UTF-8 -*-  
str = "0000000 Runoob 0000000";  
print  str.strip(  '0'  );  
\# 去除首尾字符 0   
str2 = " Runoob ";   
\# 去除首尾空格   
print  str2.strip();
```
以上实例输出结果如下：
```
     Runoob  
Runoob
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)