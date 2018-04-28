Python  chr() 函数
================

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


  描述
--

 chr() 用一个范围在 range（256）内的（就是0～255）整数作参数，返回一个对应的字符。

 ### 语法

 以下是 chr() 方法的语法:

 
```

chr(i)

```

 ### 参数

  * i -- 可以是10进制也可以是16进制的形式的数字。
  ### 返回值

 返回值是当前整数对应的ascii字符。

  实例
--

  以下展示了使用 chr() 方法的实例： 

  <pre>

>>>print chr(0x30), chr(0x31), chr(0x61) # 十六进制
0 1 a
>>> print chr(48), chr(49), chr(97) # 十进制
0 1 a
</pre>

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


