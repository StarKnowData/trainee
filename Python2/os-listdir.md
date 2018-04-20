Python os.listdir() 方法
======================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.listdir() 方法用于返回指定的文件夹包含的文件或文件夹的名字的列表。这个列表以字母顺序。 它不包括 '.' 和'..' 即使它在文件夹中。

只支持在 Unix, Windows 下使用。

### 语法

**listdir()**方法语法格式如下：
```
os.listdir(path)
```
### 参数

*   **path** \-\- 需要列出的目录路径
    

### 返回值

返回指定路径下的文件和文件夹列表。

### 实例

以下实例演示了 listdir() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 打开文件
path = "/var/www/html/"
dirs = os.listdir( path )

\# 输出所有文件和文件夹
for file in dirs:
   print file
```
执行以上程序输出结果为：
```
test.htm
stamp
faq.htm
\_vti\_txt
robots.txt
itemlisting
resumelisting
writing\_effective\_resume.htm
advertisebusiness.htm
papers
resume
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)