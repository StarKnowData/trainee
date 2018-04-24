Python file() 函数
================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

**file()** 函数用于创建一个 file 对象，它有一个别名叫 [open()](pytho-func-open.html)，更形象一些，它们是内置函数。参数是以字符串的形式传递的。

更多文件操作可参考：[Python 文件I/O](python-files-io.html)。

### 语法

以下是 file() 方法的语法:
```
file(name[, mode[, buffering]])
```
### 参数

*   name -- 文件名
*   mode -- 打开模式
*   buffering -- 0 表示不缓冲,如果为 1 表示进行行缓冲，大于 1 为缓冲区大小。

### 返回值

文件对象。

### 实例

测试文件 test.txt，内容如下：
```
RUNOOB1
RUNOOB2

>>>f = file('test.txt')
>>> f.read() 
'RUNOOB1\\nRUNOOB2\\n'
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)