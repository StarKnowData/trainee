Python globals() 函数
===================

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


  描述
--

 **globals()** 函数会以字典类型返回当前位置的全部全局变量。

 语法
--

 globals() 函数语法：

 
```

globals()

```

 参数
--

  * 无
  返回值
---

 返回全局变量的字典。

 实例
--

 以下实例展示了 globals() 的使用方法：

  <pre>

>>>a='runoob'
>>> print(globals()) # globals 函数返回一个全局变量的字典，包括所有导入的变量。
{'__builtins__': <module '__builtin__' (built-in)>, '__name__': '__main__', '__doc__': None, 'a': 'runoob', '__package__': None}
</pre>

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)

Process finished with exit code 0
