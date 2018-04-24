Python os.tcsetpgrp() 方法
========================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.tcsetpgrp() 方法用于设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。

### 语法

**tcsetpgrp()**方法语法格式如下：
```
os.tcsetpgrp(fd, pg)
```
### 参数

*   **fd** \-\- 文件描述符。
    
*   **pg** \-\- 关联的进程组。
    

### 返回值

该方法没有返回值。

### 实例

以下实例演示了 tcsetpgrp() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 显示当前目录
print "当前目录 :%s" %os.getcwd()

\# 修改目录到 /dev/tty
fd = os.open("/dev/tty",os.O_RDONLY)

f = os.tcgetpgrp(fd)

\# 显示进程组
print "关联进程组: "
print f

\# 设置进程组
os.tcsetpgrp(fd,2672)
print "done"

os.close(fd)
print "关闭文件成功!!"
```
执行以上程序输出结果为：
```
当前目录 :/tmp
关联进程组:
2672
done
关闭文件成功!!
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)