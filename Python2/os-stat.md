Python os.stat() 方法
===================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.stat() 方法用于在给定的路径上执行一个系统 stat 的调用。

### 语法

**stat()**方法语法格式如下：
```
os.stat(path)
```
### 参数

*   **path** \-\- 指定路径
    

### 返回值

stat 结构:

*   **st_mode:** inode 保护模式
*   **st_ino:** inode 节点号。
*   **st_dev:** inode 驻留的设备。
*   **st_nlink:** inode 的链接数。
*   **st_uid:** 所有者的用户ID。
*   **st_gid:** 所有者的组ID。
*   **st_size:** 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
*   **st_atime:** 上次访问的时间。
*   **st_mtime:** 最后一次修改的时间。
*   **st_ctime:** 由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。

### 实例

以下实例演示了 stat() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 显示文件 "a2.py" 信息
statinfo = os.stat('a2.py')

print statinfo
```
执行以上程序输出结果为：
```
posix.stat\_result(st\_mode=33188, st\_ino=3940649674337682L, st\_dev=277923425L, st
\_nlink=1, st\_uid=400, st\_gid=401, st\_size=335L, st\_atime=1330498089, st\_mtime=13
30498089, st_ctime=1330498089)
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)