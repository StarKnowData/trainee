Python os.fdatasync() 方法
========================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.fdatasync() 方法用于强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。如果你需要刷新缓冲区可以使用该方法。

Unix上可用。

### 语法

**fdatasync()**方法语法格式如下：
```
os.fdatasync(fd);
```
### 参数

*   **fd** \-\- 文件描述符
    

### 返回值

该方法没有返回值。

### 实例

以下实例演示了 fdatasync() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 打开文件 "/tmp/foo.txt"
fd = os.open( "foo.txt", os.O\_RDWR|os.O\_CREAT )

\# 写入字符串
os.write(fd, "This is test")

\# 使用 fdatasync() 方法
os.fdatasync(fd)

\# 读取文件
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print "读取的字符是 : ", str

\# 关闭文件
os.close( fd )

print "关闭文件成功!!"
```
执行以上程序输出结果为：
```
读取的字符是 :  This is test
关闭文件成功!!
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)