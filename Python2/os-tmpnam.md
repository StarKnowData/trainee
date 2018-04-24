Python os.tmpnam() 方法
=====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.tmpnam() 方法用于为创建一个临时文件返回一个唯一的路径。

### 语法

**tmpnam()**方法语法格式如下：
```
os.tmpnam
```
### 参数

*   无
    

### 返回值

返回一个唯一的路径。

### 实例

以下实例演示了 tmpnam() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 生成临时路径
tmpfn = os.tmpnam()

print "这是一个唯一的路径:"
print tmpfn
```
执行以上程序输出结果为：
```
这是一个唯一的路径:
/tmp/fileUFojpd
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)