Python type() 函数
================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

type() 函数如果你只有第一个参数则返回对象的类型，三个参数返回新的类型对象。

> isinstance() 与 type() 区别：
> 
> *   type() 不会认为子类是一种父类类型，不考虑继承关系。
>     
> *   isinstance() 会认为子类是一种父类类型，考虑继承关系。
>     
> 
> 如果要判断两个类型是否相同推荐使用 isinstance()。

### 语法

以下是 type() 方法的语法:
```
class type(name, bases, dict)
```
### 参数

*   name -- 类的名称。
*   bases -- 基类的元组。
*   dict -- 字典，类内定义的命名空间变量。

### 返回值

一个参数返回对象类型, 三个参数，返回新的类型对象。

* * *

实例
--

以下展示了使用 type 函数的实例：
```
\# 一个参数实例 
>>\> type(1) <type  'int'> >>\> type('runoob') <type  'str'> >>\> type(\[2\]) <type  'list'> >>\> type({0:'zero'}) <type  'dict'> >>\> x = 1 >>\> type(  x  ) == int  \# 判断类型是否相等  True  \# 三个参数 >>\> class  X(object): ... a = 1 ... >>\> X = type('X', (object,), dict(a=1))  \# 产生一个新的类型 X >>\> X <class  '\_\_main\_\_.X'>
```
type() 与 isinstance()区别：
------------------------
```
class  A: pass  class  B(A): pass  isinstance(A(), A)  \# returns True  type(A()) == A  \# returns True  isinstance(B(), A)  \# returns True  type(B()) == A  \# returns False
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)