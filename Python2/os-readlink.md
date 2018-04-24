Python os.readlink() 方法
=======================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.readlink() 方法用于返回软链接所指向的文件。可能返回绝对火相对路径。

在Unix中有效

### 语法

**readlink()**方法语法格式如下：
```
os.readlink(path)
```
### 参数

*   **path** \-\- 要查找的软链接路径
    

### 返回值

返回软链接所指向的文件

### 实例

以下实例演示了 readlink() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os

src = '/usr/bin/python'
dst = '/tmp/python'

\# 创建软链接
os.symlink(src, dst)

\# 使用软链接显示源链接
path = os.readlink( dst )
print path
```
执行以上程序输出结果为：
```
/usr/bin/python
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)