Python os.ttyname() 方法
======================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.ttyname() 方法用于返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。

### 语法

**ttyname()**方法语法格式如下：
```
os.ttyname(fd)
```
### 参数

*   **fd** \-\- 文件描述符
    

### 返回值

返回一个字符串，它表示与文件描述符fd 关联的终端设备。

### 实例

以下实例演示了 ttyname() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 显示当前目录
print "当前目录 :%s" %os.getcwd()

\# 修改目录为 /dev/tty
fd = os.open("/dev/tty",os.O_RDONLY)

p = os.ttyname(fd)
print "关联的终端为: "
print p
print "done!!"

os.close(fd)
print "关闭文件成功!!"
```
执行以上程序输出结果为：
```
当前目录 :/tmp
关联的终端为:
/dev/tty
done!!
关闭文件成功!!
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)