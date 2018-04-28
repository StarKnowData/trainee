Python complex() 函数
===================

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


  描述
--

 **complex()** 函数用于创建一个值为 real + imag * j 的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。。

 语法
--

 complex 语法：

 
```

class complex([real[, imag]])

```

  参数说明：

  * real -- int, long, float或字符串；
 * imag -- int, long, float；
  返回值
---

 返回一个复数。

 实例
--

 以下实例展示了 complex 的使用方法：

  <pre>

>>>complex(1, 2)
(1 + 2j)
 
>>> complex(1) # 数字
(1 + 0j)
 
>>> complex("1") # 当做字符串处理
(1 + 0j)
# 注意：这个地方在"+"号两边不能有空格，也就是不能写成"1 + 2j"，应该是"1+2j"，否则会报错
>>> complex("1+2j")
(1 + 2j)
</pre>

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)

Process finished with exit code 0
