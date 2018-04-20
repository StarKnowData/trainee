Python basestring() 函数
======================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

**basestring()** 方法是 str 和 unicode 的超类（父类），也是抽象类，因此不能被调用和实例化，但可以被用来判断一个对象是否为 str 或者 unicode 的实例，isinstance(obj, basestring) 等价于 isinstance(obj, (str, unicode))。

### 语法

以下是 basestring() 方法的语法:
```
basestring()
```
### 参数

*   无

### 返回值

无。

* * *

实例
--

以下展示了使用 basestring 函数的实例：
```
>>>isinstance("Hello world", str)  True >>\> isinstance("Hello world", basestring)  True
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)