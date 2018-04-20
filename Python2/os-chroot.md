Python os.chroot() 方法
=====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.chroot() 方法用于更改当前进程的根目录为指定的目录，使用该函数需要管理员权限。

### 语法

**chroot()**方法语法格式如下：
```
os.chroot(path);
```
### 参数

*   **path** \-\- 要设置为根目录的目录。
    

### 返回值

该方法没有返回值。

### 实例

以下实例演示了 chroot() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 设置根目录为 /tmp

os.chroot("/tmp")

print "修改根目录成功!!"
```
执行以上程序输出结果为：
```
修改根目录成功!!
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)