Python os.fsync() 方法
====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.fsync() 方法强制将文件描述符为fd的文件写入硬盘。在Unix, 将调用fsync()函数;在Windows, 调用 _commit()函数。

如果你准备操作一个Python文件对象f, 首先f.flush(),然后os.fsync(f.fileno()), 确保与f相关的所有内存都写入了硬盘.在unix，Windows中有效。

Unix、Windows上可用。

### 语法

**fsync()**方法语法格式如下：
```
os.fsync(fd)
```
### 参数

*   **fd** \-\- 文件的描述符。
    

### 返回值

该方法没有返回值。

### 实例

以下实例演示了 fsync() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 打开文件
fd = os.open( "foo.txt", os.O\_RDWR|os.O\_CREAT )

\# 写入字符串
os.write(fd, "This is test")

\# 使用 fsync() 方法.
os.fsync(fd)

\# 读取内容
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print "读取的字符串为 : ", str

\# 关闭文件
os.close( fd)

print "关闭文件成功!!"
```
执行以上程序输出结果为：
```
读取的字符串为 :  This is test
关闭文件成功!!
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)