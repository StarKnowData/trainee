Python capitalize()方法
=====================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python capitalize()将字符串的第一个字母变成大写,其他字母变小写。对于 8 位字节编码需要根据本地环境。

语法
--

capitalize()方法语法：
```
str.capitalize()
```
参数
--

*   无。

返回值
---

该方法返回一个首字母大写的字符串。

实例
--

以下实例展示了capitalize()方法的实例：
```
>>>s = 'a, B'  
>>\> s.capitalize()    
'A, b'   

>>\> s = ' a, B'  \# a 前面有空格 
>>\> s.capitalize()    
' a, b'    
 
>>\> s = 'a, BCD'   
>>\> s.capitalize()   
'A, bcd'
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)
