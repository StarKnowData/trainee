Python os.unlink() 方法
=====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.unlink() 方法用于删除文件,如果文件是一个目录则返回一个错误。

### 语法

**unlink()**方法语法格式如下：
```
os.unlink(path)
```
### 参数

*   **path** \-\- 删除的文件路径
    

### 返回值

该方法没有返回值。

### 实例

以下实例演示了 unlink() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 列出目录
print "目录为: %s" %os.listdir(os.getcwd())

os.unlink("aa.txt")

\# 删除后的目录
print "删除后的目录为 : %s" %os.listdir(os.getcwd())
```
执行以上程序输出结果为：
```
目录为:
 \[ 'a1.txt','aa.txt','resume.doc'\]
删除后的目录为 : 
\[ 'a1.txt','resume.doc' \]
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)