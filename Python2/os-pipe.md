Python os.pipe() 方法
===================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.pipe() 方法用于创建一个管道, 返回一对文件描述符(r, w) 分别为读和写。

### 语法

**pipe()**方法语法格式如下：
```
os.pipe()
```
### 参数

*   无
    

### 返回值

返回文件描述符对。

### 实例

以下实例演示了 pipe() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

print "The child will write text to a pipe and "
print "the parent will read the text written by child..."

\# file descriptors r, w for reading and writing
r, w = os.pipe() 

processid = os.fork()
if processid:
    # This is the parent process 
    # Closes file descriptor w
    os.close(w)
    r = os.fdopen(r)
    print "Parent reading"
    str = r.read()
    print "text =", str   
    sys.exit(0)
else:
    # This is the child process
    os.close(r)
    w = os.fdopen(w, 'w')
    print "Child writing"
    w.write("Text written by child...")
    w.close()
    print "Child closing"
    sys.exit(0)
```
执行以上程序输出结果为：
```
The child will write text to a pipe and
the parent will read the text written by child...
Parent reading
Child writing
Child closing
text = Text written by child...
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)