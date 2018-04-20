Python os.fstat() 方法
====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.fstat() 方法用于返回文件描述符fd的状态，类似 stat()。

Unix，Windows上可用。

fstat 方法返回的结构:

*   **st_dev:** 设备信息
    
*   **st_ino:** 文件的i-node值
    
*   **st_mode:** 文件信息的掩码，包含了文件的权限信息，文件的类型信息(是普通文件还是管道文件，或者是其他的文件类型)
    
*   **st_nlink:** 硬连接数
    
*   **st_uid:** 用户ID
    
*   **st_gid:** 用户组 ID
    
*   **st_rdev:** 设备 ID (如果指定文件)
    
*   **st_size:** 文件大小，以byte为单位
    
*   **st_blksize:** 系统 I/O 块大小
    
*   **st_blocks:** 文件的是由多少个 512 byte 的块构成的
    
*   **st_atime:** 文件最近的访问时间
    
*   **st_mtime:** 文件最近的修改时间
    
*   **st_ctime:** 文件状态信息的修改时间（不是文件内容的修改时间）
    

### 语法

**fstat()**方法语法格式如下：
```
os.fstat(fd)
```
### 参数

*   **fd** \-\- 文件的描述符。
    

### 返回值

返回文件描述符fd的状态。

### 实例

以下实例演示了 fstat() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 打开文件
fd = os.open( "foo.txt", os.O\_RDWR|os.O\_CREAT )

\# 获取元组
info = os.fstat(fd)

print "文件信息 :", info

\# 获取文件 uid
print "文件 UID :%d" % info.st_uid

\# 获取文件 gid
print "文件 GID  :%d" % info.st_gid

\# 关闭文件
os.close( fd)
```
执行以上程序输出结果为：
```
文件信息 : (33261, 3753776L, 103L, 1, 0, 0, 
            102L, 1238783197, 1238786767, 1238786767)
文件 UID :0
文件 GID :0
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)