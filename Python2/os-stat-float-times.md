Python os.stat\_float\_times() 方法
=================================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.stat\_float\_times()
方法用于决定stat_result是否以float对象显示时间戳。

### 语法

**stat\_float\_times()**方法语法格式如下：
```
os.stat_float_times([newvalue])
```
### 参数

*   **newvalue** \-\- 如果为 True, 调用 stat() 返回 floats,如果 False, 调用 stat 返回 ints。如果没有该参数返回当前设置。
    

### 返回值

返回 True 或 False。

### 实例

以下实例演示了 stat\_float\_times() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# Stat 信息
statinfo = os.stat('a2.py')

print statinfo
statinfo = os.stat\_float\_times()
print statinfo
```
执行以上程序输出结果为：
```
posix.stat\_result(st\_mode=33188, st\_ino=3940649674337682L, st\_dev=277923425L, 
st\_nlink=1, st\_uid=400, st\_gid=401, st\_size=335L, st\_atime=1330498089, st\_mtime=13
30498089, st_ctime=1330498089)
True
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)