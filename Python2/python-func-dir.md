Python dir() 函数
===============

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


  描述
--

 **dir()** 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；带参数时，返回参数的属性、方法列表。如果参数包含方法\_\_dir\_\_()，该方法将被调用。如果参数不包含\_\_dir\_\_()，该方法将最大限度地收集参数信息。

 语法
--

 dir 语法：

 
```

dir([object])

```

  参数说明：

  * object -- 对象、变量、类型。
  返回值
---

 返回模块的属性列表。

 实例
--

 以下实例展示了 dir 的使用方法：

  <pre>

>>>dir() #  获得当前模块的属性列表
['__builtins__', '__doc__', '__name__', '__package__', 'arr', 'myslice']
>>> dir([ ]) # 查看列表的方法
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
>>>
</pre>

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)

Process finished with exit code 0
