Python os.utime() 方法
====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.utime() 方法用于设置指定路径文件最后的修改和访问时间。

在Unix，Windows中有效。

### 语法

**utime()**方法语法格式如下：
```
os.utime(path, times)
```
### 参数

*   **path** \-\- 文件路径
    
*   **times** \-\- 如果时间是 None, 则文件的访问和修改设为当前时间 。 否则, 时间是一个 2-tuple数字, (atime, mtime) 用来分别作为访问和修改的时间。
    

### 返回值

该方法没有返回值。

### 实例

以下实例演示了 utime() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 显示文件的 stat 信息
stinfo = os.stat('a2.py')
print stinfo

\# 使用 os.stat 来接收文件的访问和修改时间
print "a2.py 的访问时间: %s" %stinfo.st_atime
print "a2.py 的修改时间: %s" %stinfo.st_mtime

\# 修改访问和修改时间
os.utime("a2.py",(1330712280, 1330712292))
print "done!!"
```
执行以上程序输出结果为：
```
posix.stat\_result(st\_mode=33188, st\_ino=3940649674337682L, st\_dev=277923425L, st
\_nlink=1, st\_uid=400, st\_gid=401, st\_size=335L, st\_atime=1330498070, st\_mtime=13
30498074, st_ctime=1330498065)
a2.py 的访问时间: 1330498070
a2.py 的修改时间: 1330498074
done!!
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)