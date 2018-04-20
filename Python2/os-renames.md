Python os.renames() 方法
======================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.renames() 方法用于递归重命名目录或文件。类似rename()。

### 语法

**renames()**方法语法格式如下：
```
os.renames(old, new)
```
### 参数

*   **old** \-\- 要重命名的目录
    
*   **new** --文件或目录的新名字。甚至可以是包含在目录中的文件，或者完整的目录树。
    

### 返回值

该方法没有返回值

### 实例

以下实例演示了 renames() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys
print "当前目录为: %s" %os.getcwd()

\# 列出目录
print "目录为: %s"%os.listdir(os.getcwd())

\# 重命名 "aa1.txt"
os.renames("aa1.txt","newdir/aanew.txt")

print "重命名成功。"

\# 列出重命名的文件 "aa1.txt"
print "目录为: %s" %os.listdir(os.getcwd())
```
执行以上程序输出结果为：
```
当前目录为: /tmp
目录为:
 \[  'a1.txt','resume.doc','a3.py','aa1.txt','Administrator','amrood.admin' \]
重命名成功。
目录为:
 \[  'a1.txt','resume.doc','a3.py','Administrator','amrood.admin' \]
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)