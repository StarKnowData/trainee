Python os.statvfs() 方法
======================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.statvfs() 方法用于返回包含文件描述符fd的文件的文件系统的信息。

### 语法

**statvfs()**方法语法格式如下：
```
os.statvfs([path])
```
### 参数

*   **path** \-\- 文件路径。
    

### 返回值

返回的结构:

*   **f_bsize:** 文件系统块大小
    
*   **f_frsize:** 分栈大小
    
*   **f_blocks:** 文件系统数据块总数
    
*   **f_bfree:** 可用块数
    
*   **f_bavail:**非超级用户可获取的块数
    
*   **f_files:** 文件结点总数
    
*   **f_ffree:** 可用文件结点数
    
*   **f_favail:** 非超级用户的可用文件结点数
    
*   **f_fsid:** 文件系统标识 ID
    
*   **f_flag:** 挂载标记
    
*   **f_namemax:** 最大文件长度
    

### 实例

以下实例演示了 statvfs() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 显示 "a1.py" 文件的 statvfs 信息
stinfo = os.statvfs('a1.py')

print stinfo
```
执行以上程序输出结果为：
```
posix.statvfs\_result(f\_bsize=4096, f\_frsize=4096, f\_blocks=1909350L, f_bfree=1491513L,
f\_bavail=1394521L, f\_files=971520L, f\_ffree=883302L, f\_fvail=883302L, f_flag=0,
f_namemax=255)
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)