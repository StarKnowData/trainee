Python hex() 函数
===============

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

**hex()** 函数用于将10进制整数转换成16进制，以字符串形式表示。

语法
--

hex 语法：
```
hex(x)
```
参数说明：

*   x -- 10进制整数

返回值
---

返回16进制数，以字符串形式表示。

实例
--

以下实例展示了 hex 的使用方法：
```
>>>hex(255)  '0xff' >>\> hex(-42)  '-0x2a' >>\> hex(1L)  '0x1L' >>\> hex(12)  '0xc' >>\> type(hex(12)) <class  'str'\> \# 字符串
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)