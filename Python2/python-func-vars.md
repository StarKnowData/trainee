Python vars() 函数
================

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


  描述
--

 **vars()** 函数返回对象object的属性和属性值的字典对象。

 语法
--

 vars() 函数语法：

 
```

vars([object])

```

 参数
--

  * object -- 对象
  返回值
---

 返回对象object的属性和属性值的字典对象，如果没有参数，就打印当前调用位置的属性和属性值 类似 locals()。

 实例
--

 以下实例展示了 vars() 的使用方法：

  <pre>

>>>print(vars())
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, '__package__': None}
>>> class Runoob:
...     a = 1
... 
>>> print(vars(Runoob))
{'a': 1, '__module__': '__main__', '__doc__': None}
>>> runoob = Runoob()
>>> print(vars(runoob))
{}
</pre>

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


