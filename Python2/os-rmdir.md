Python os.rmdir() 方法
====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.rmdir() 方法用于删除指定路径的目录。仅当这文件夹是空的才可以, 否则, 抛出OSError。

### 语法

**rmdir()**方法语法格式如下：
```
os.rmdir(path)
```
### 参数

*   **path** \-\- 要删除的目录路径
    

### 返回值

该方法没有返回值

### 实例

以下实例演示了 rmdir() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 列出目录
print "目录为: %s"%os.listdir(os.getcwd())

\# 删除路径
os.rmdir("mydir")

\# 列出重命名后的目录
print "目录为: %s" %os.listdir(os.getcwd())
```
执行以上程序输出结果为：
```
目录为:
\[  'a1.txt','resume.doc','a3.py','mydir' \]
目录为:
\[  'a1.txt','resume.doc','a3.py' \]
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)