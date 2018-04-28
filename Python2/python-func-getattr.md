Python getattr() 函数
===================

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


  描述
--

 **getattr()** 函数用于返回一个对象属性值。

 语法
--

 getattr 语法：

 
```

getattr(object, name[, default])

```

 参数
--

  * object -- 对象。
 * name -- 字符串，对象属性。
 * default -- 默认返回值，如果不提供该参数，在没有对应属性时，将触发 AttributeError。
  返回值
---

 返回对象属性值。

 实例
--

 以下实例展示了 getattr 的使用方法：

  <pre>

>>>class A(object):
...     bar = 1
... 
>>> a = A()
>>> getattr(a, 'bar') # 获取属性 bar 值
1
>>> getattr(a, 'bar2') # 属性 bar2 不存在，触发异常
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'A' object has no attribute 'bar2'
>>> getattr(a, 'bar2', 3) # 属性 bar2 不存在，但设置了默认值
3
>>>
</pre>

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


