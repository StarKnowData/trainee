Python reload() 函数
==================

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


  描述
--

 **reload()** 用于重新载入之前载入的模块。

 语法
--

 reload() 函数语法：

 
```

reload(module)

```

 参数
--

  * module -- 模块对象。
  返回值
---

 返回模块对象。

 实例
--

 以下实例展示了 reload() 的使用方法：

  重新载入 sys 模块，并设置默认编码为 utf8
-------------------------

 <pre>

>>>import sys
>>> sys.getdefaultencoding() # 当前默认编码
'ascii'
>>> reload(sys) # 使用 reload
<module 'sys' (built-in)>
>>> sys.setdefaultencoding('utf8') # 设置编码
>>> sys.getdefaultencoding()
'utf8'
>>>
</pre>

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


