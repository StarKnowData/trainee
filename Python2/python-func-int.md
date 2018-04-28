Python  int() 函数
================

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


  描述
--

 int() 函数用于将一个字符串或数字转换为整型。

 ### 语法

 以下是 int() 方法的语法:

 
```

class int(x, base=10)

```

 ### 参数

  * x -- 字符串或数字。
 * base -- 进制数，默认十进制。
  ### 返回值

 返回整型数据。

  实例
--

  以下展示了使用 int() 方法的实例： 

  <pre>

>>>int() # 不传入参数时，得到结果0
0
>>> int(3)
3
>>> int(3.6)
3
>>> int('12',16) # 如果是带参数base的话，12要以字符串的形式进行输入，12 为 16进制
18
>>> int('0xa',16)
10  
>>> int('10',8)
8
</pre>

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)

