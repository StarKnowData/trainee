Python File fileno() 方法
=======================

 [![Python File(文件) 方法](../images/up.gif) Python File(文件) 方法](file-methods.html)

* * *

### 概述

**fileno()** 方法返回一个整型的文件描述符(file descriptor FD 整型)，可用于底层操作系统的 I/O 操作。

### 语法

fileno() 方法语法如下：
```
fileObject.fileno(); 
```
### 参数

*   **无**
    

### 返回值

返回文件描述符。

### 实例

以下实例演示了 fileno() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

\# 打开文件
fo = open("runoob.txt", "wb")
print "文件名为: ", fo.name

fid = fo.fileno()
print "文件描述符为: ", fid

\# 关闭文件
fo.close()
```
以上实例输出结果为：
```
文件名为:  runoob.txt
文件描述符为:  3
```
 [![Python File(文件) 方法](../images/up.gif) Python File(文件) 方法](file-methods.html)