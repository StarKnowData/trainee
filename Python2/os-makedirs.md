Python os.makedirs() 方法
=======================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.makedirs() 方法用于递归创建目录。像 mkdir(), 但创建的所有intermediate-level文件夹需要包含子目录。

### 语法

**makedirs()**方法语法格式如下：
```
os.makedirs(path, mode=0o777)
```
### 参数

*   **path** \-\- 需要递归创建的目录。
    
*   **mode** \-\- 权限模式。
    

### 返回值

该方法没有返回值。

### 实例

以下实例演示了 makedirs() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 创建的目录
path = "/tmp/home/monthly/daily"

os.makedirs( path, 0755 );

print "路径被创建"
```
执行以上程序输出结果为：
```
路径被创建
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)