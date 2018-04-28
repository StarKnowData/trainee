Python  ord() 函数
================

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


  描述
--

 ord() 函数是 chr() 函数（对于8位的ASCII字符串）或 unichr() 函数（对于Unicode对象）的配对函数，它以一个字符（长度为1的字符串）作为参数，返回对应的 ASCII 数值，或者 Unicode 数值，如果所给的 Unicode 字符超出了你的 Python 定义范围，则会引发一个 TypeError 的异常。

 ### 语法

 以下是 ord() 方法的语法:

 
```

ord(c)

```

 ### 参数

  * c -- 字符。
  ### 返回值

 返回值是对应的十进制整数。

  实例
--

  以下展示了使用 ord() 方法的实例： 

  <pre>

>>>ord('a')
97
>>> ord('b')
98
>>> ord('c')
99
</pre>

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)

