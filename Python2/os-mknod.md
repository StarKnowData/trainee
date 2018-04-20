Python os.mknod() 方法
====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.mknod() 方法用于创建一个指定文件名的文件系统节点（文件，设备特别文件或者命名pipe）。

### 语法

**mknod()**方法语法格式如下：
```
os.mknod(filename[, mode=0600[, device=0]])
```
### 参数

*   **filename** \-\- 创建的文件系统节点
    
*   **mode** \-\- mode指定创建或使用节点的权限, 组合 (或者bitwise) stat.S\_IFREG, stat.S\_IFCHR, stat.S\_IFBLK, 和stat.S\_IFIFO (这些常数在stat模块). 对于 stat.S\_IFCHR和stat.S\_IFBLK, 设备定义了 最新创建的设备特殊文件 (可能使用 os.makedev()),其它都将忽略。
    
*   **device** \-\- 可选，指定创建文件的设备
    

### 返回值

该方法没有返回值。

### 实例

以下实例演示了 mknod() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os
import stat

filename = '/tmp/tmpfile'
mode = 0600|stat.S_IRUSR

\# 文件系统节点指定不同模式
os.mknod(filename, mode)
```
执行以上程序输出结果为：
```
-rw-------. 1 root   root         0 Apr 30 02:38 tmpfile
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)