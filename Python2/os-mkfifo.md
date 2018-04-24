Python os.mkfifo() 方法
=====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.mkfifo() 方法用于创建指令路径的管道，并设置权限模式。默认的模式为 0666 (八进制)。

### 语法

**mkfifo()**方法语法格式如下：
```
os.mkfifo(path[, mode])
```
### 参数

*   **path** \-\- 要创建的目录
    
*   **mode** \-\- 要为目录设置的权限数字模式
    

### 返回值

该方法没有返回值。

### 实例

以下实例演示了 mkfifo() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 创建的目录
path = "/tmp/hourly"

os.mkfifo( path, 0644 )

print "路径被创建"
```
执行以上程序输出结果为：
```
路径被创建
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)