Python os.chdir() 方法
====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.chdir() 方法用于改变当前工作目录到指定的路径。

### 语法

**chdir()**方法语法格式如下：
```
os.chdir(path)
```
### 参数

*   **path** \-\- 要切换到的新路径。
    

### 返回值

如果允许访问返回 True , 否则返回False。

### 实例

以下实例演示了 chdir() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

path = "/tmp"

\# 查看当前工作目录
retval = os.getcwd()
print "当前工作目录为 %s" % retval

\# 修改当前工作目录
os.chdir( path )

\# 查看修改后的工作目录
retval = os.getcwd()

print "目录修改成功 %s" % retval
```
执行以上程序输出结果为：
```
当前工作目录为 /www
目录修改成功 /tmp
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)