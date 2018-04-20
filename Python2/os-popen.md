Python os.popen() 方法
====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.popen() 方法用于从一个命令打开一个管道。

在Unix，Windows中有效

### 语法

**popen()**方法语法格式如下：
```
os.popen(command[, mode[, bufsize]])
```
### 参数

*   **command** \-\- 使用的命令。
    
*   **mode** \-\- 模式权限可以是 'r'(默认) 或 'w'。
    
*   **bufsize** \-\- 指明了文件需要的缓冲大小：0意味着无缓冲；1意味着行缓冲；其它正值表示使用参数大小的缓冲（大概值，以字节为单位）。负的bufsize意味着使用系统的默认值，一般来说，对于tty设备，它是行缓冲；对于其它文件，它是全缓冲。如果没有改参数，使用系统的默认值。
    

### 返回值

返回一个文件描述符号为fd的打开的文件对象

### 实例

以下实例演示了 popen() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 使用 mkdir 命令
a = 'mkdir nwdir'

b = os.popen(a,'r',1)

print b
```
执行以上程序输出结果为：
```
open file 'mkdir nwdir', mode 'r' at 0x81614d0
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)