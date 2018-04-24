Python File close() 方法
======================

 [![Python File(文件) 方法](../images/up.gif) Python File(文件) 方法](file-methods.html)

* * *

### 概述

**close()** 方法用于关闭一个已打开的文件。关闭后的文件不能再进行读写操作， 否则会触发 _ValueError_ 错误。 close() 方法允许调用多次。

当 file 对象，被引用到操作另外一个文件时，Python 会自动关闭之前的 file 对象。 使用 close() 方法关闭文件是一个好的习惯。

### 语法

close() 方法语法如下：
```
fileObject.close();
```
### 参数

*   **无**
    

### 返回值

该方法没有返回值。

### 实例

以下实例演示了 close() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

\# 打开文件
fo = open("runoob.txt", "wb")
print "文件名为: ", fo.name

\# 关闭文件
fo.close()
```
以上实例输出结果为：
```
文件名为:  runoob.txt
```
 [![Python File(文件) 方法](../images/up.gif) Python File(文件) 方法](file-methods.html)