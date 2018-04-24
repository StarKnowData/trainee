Python os.openpty() 方法
======================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.openpty() 方法用于打开一个新的伪终端对。返回 pty 和 tty的文件描述符。

### 语法

**openpty()**方法语法格式如下：
```
os.openpty()
```
### 参数

*   无

### 返回值

返回文件描述符对，主从。

### 实例

以下实例演示了 openpty() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os

\# 主 pty, 从 tty
m,s = os.openpty()

print m
print s

\# 显示终端名
s = os.ttyname(s)
print m
print s
```
执行以上程序输出结果为：
```
3
4
3
/dev/pty0
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)