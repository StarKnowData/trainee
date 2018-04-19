Python center()方法
=================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python center() 返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。默认填充字符为空格。

语法
--

center()方法语法：
```
str.center(width\[, fillchar\])
```
参数
--

*   width -- 字符串的总宽度。
*   fillchar -- 填充字符。

返回值
---

该方法返回一个原字符串居中,并使用空格填充至长度 width 的新字符串。

实例
--

以下实例展示了center()方法的实例：
```
>>>str = 'runoob'  
>>\>str.center(20, '*')   

'\*\*\*\*\*\*\*runoob\*\*\*\*\*\*\*'   
>>\> str.center(20)   
' runoob '  
>>>
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)
