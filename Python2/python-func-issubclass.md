Python issubclass() 函数
======================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

**issubclass()** 方法用于判断参数 class 是否是类型参数 classinfo 的子类。

### 语法

以下是 issubclass() 方法的语法:
```
issubclass(class, classinfo)
```
### 参数

*   class -- 类。
*   classinfo -- 类。

### 返回值

如果 class 是 classinfo 的子类返回 True，否则返回 False。

* * *

实例
--

以下展示了使用 basestring 函数的实例：
```
#!/usr/bin/python  
\# -*- coding: UTF-8 -*- 
class  A: pass  class  B(A): pass 
print(issubclass(B,A))
\# 返回 True
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)