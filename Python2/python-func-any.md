Python  any() 函数
================

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


  描述
--

 any() 函数用于判断给定的可迭代参数 iterable 是否全部为空对象，如果都为空、0、false，则返回 False，如果不都为空、0、false，则返回 True。

 函数等价于：


```

def any(iterable):
    for element in iterable:
        if element:
            return True
    return False

```

 Python 2.5 以上版本可用。

 ### 语法

 以下是 any() 方法的语法:

 
```

any(iterable)

```

 ### 参数

  * iterable -- 元组或列表。
  ### 返回值

 如果都为空、0、false，则返回false，如果不都为空、0、false，则返回true。

  实例
--

  以下展示了使用 any() 方法的实例： 

  <pre>

>>>any(['a', 'b', 'c', 'd']) # 列表list，元素都不为空或0
True
 
>>> any(['a', 'b', '', 'd']) # 列表list，存在一个为空的元素
True
 
>>> any([0, '', False]) # 列表list,元素全为0,'',false
False
 
>>> any(('a', 'b', 'c', 'd')) # 元组tuple，元素都不为空或0
True
 
>>> any(('a', 'b', '', 'd')) # 元组tuple，存在一个为空的元素
True
 
>>> any((0, '', False)) # 元组tuple，元素全为0,'',false
False
  
>>> any([]) # 空列表
False
 
>>> any(()) # 空元组
False
</pre>

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)

Process finished with exit code 0
