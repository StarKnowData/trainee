Python execfile() 函数
====================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

execfile() 函数可以用来执行一个文件。

### 语法

以下是 execfile() 方法的语法:
```
execfile(filename[, globals[, locals]])
```
### 参数

*   filename -- 文件名。
*   globals -- 变量作用域，全局命名空间，如果被提供，则必须是一个字典对象。
*   locals -- 变量作用域，局部命名空间，如果被提供，可以是任何映射对象。

### 返回值

返回表达式执行结果。

* * *

实例
--

以下展示了使用 execfile 函数的实例：
```
假设文件 hello.py，内容如下：

print('runoob');

execfile 调用该文件
--------------

>>>execfile('hello.py')  runoob
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)