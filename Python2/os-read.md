Python os.read() 方法
===================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.read() 方法用于从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。

在Unix，Windows中有效

### 语法

**read()**方法语法格式如下：
```
os.read(fd,n)
```
### 参数

*   **fd** \-\- 文件描述符。
    
*   **n** \-\- 读取的字节。
    

### 返回值

返回包含读取字节的字符串

### 实例

以下实例演示了 read() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys
\# 打开文件
fd = os.open("f1.txt",os.O_RDWR)
    
\# 读取文本
ret = os.read(fd,12)
print ret

\# 关闭文件
os.close(fd)
print "关闭文件成功!!"
```
执行以上程序输出结果为：
```
This is test
关闭文件成功!!
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)