Python os.remove() 方法
=====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.remove() 方法用于删除指定路径的文件。如果指定的路径是一个目录，将抛出OSError。

在Unix, Windows中有效

### 语法

**remove()**方法语法格式如下：
```
os.remove(path)
```
### 参数

*   **path** \-\- 要移除的文件路径
    

### 返回值

该方法没有返回值

### 实例

以下实例演示了 remove() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 列出目录
print "目录为: %s" %os.listdir(os.getcwd())

\# 移除
os.remove("aa.txt")

\# 移除后列出目录
print "移除后 : %s" %os.listdir(os.getcwd())
```
执行以上程序输出结果为：
```
目录为:
\[ 'a1.txt','aa.txt','resume.doc' \]
移除后 : 
\[ 'a1.txt','resume.doc' \]
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)