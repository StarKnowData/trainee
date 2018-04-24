Python os.removedirs() 方法
=========================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.removedirs() 方法用于递归删除目录。像rmdir(), 如果子文件夹成功删除, removedirs()才尝试它们的父文件夹,直到抛出一个error(它基本上被忽略,因为它一般意味着你文件夹不为空)。

### 语法

**removedirs()**方法语法格式如下：
```
os.removedirs(path)
```
### 参数

*   **path** \-\- 要移除的目录路径
    

### 返回值

该方法没有返回值

### 实例

以下实例演示了 removedirs() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 列出目录
print "目录为: %s" %os.listdir(os.getcwd())

\# 移除
os.removedirs("/test")

\# 列出移除后的目录
print "移除后目录为:" %os.listdir(os.getcwd())
```
执行以上程序输出结果为：
```
目录为:
\[  'a1.txt','resume.doc','a3.py','test' \]
移除后目录为:
\[  'a1.txt','resume.doc','a3.py' \]
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)