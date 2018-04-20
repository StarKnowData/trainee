Python os.fchdir() 方法
=====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.fchdir() 方法通过文件描述符改变当前工作目录。

Unix, Windows 上可用。

### 语法

**fchdir()**方法语法格式如下：
```
os.fchdir(fd);
```
### 参数

*   **fd** \-\- 文件描述符
    

### 返回值

该方法没有返回值。

### 实例

以下实例演示了 fchdir() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 首先到目录 "/var/www/html" 
os.chdir("/var/www/html" )

\# 输出当前目录
print "当前工作目录为 : %s" % os.getcwd()

\# 打开新目录 "/tmp"
fd = os.open( "/tmp", os.O_RDONLY )

\# 使用 os.fchdir() 方法修改到新目录
os.fchdir(fd)

\# 输出当前目录
print "当前工作目录为 : %s" % os.getcwd()

\# 关闭打开的目录
os.close( fd )
```
执行以上程序输出结果为：
```
当前工作目录为 : /var/www/html
当前工作目录为 : /tmp
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)