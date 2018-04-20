Python os.fdopen() 方法
=====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.fdopen() 方法用于通过文件描述符 fd 创建一个文件对象，并返回这个文件对象。

Unix, Windows上可用。

### 语法

**fdopen()**方法语法格式如下：
```
os.fdopen(fd, [, mode[, bufsize]]);
```
### 参数

*   **fd** \-\- 打开的文件的描述符，在Unix下，描述符是一个小整数。
    
*   **mode** \-\- 可选，和bufsize参数和Python内建的open函数一样，mode参数可以指定『r,w,a,r+,w+,a+,b』等，表示文件的是只读的还是可以读写的，以及打开文件是以二进制还是文本形式打开。这些参数和C语言中的<stdio.h>中fopen函数中指定的mode参数类似。
    
*   **bufsize** \-\- 可选，指定返回的文件对象是否带缓冲：bufsize=0，表示没有带缓冲；bufsize=1，表示该文件对象是行缓冲的；bufsize=正数，表示使用一个指定大小的缓冲冲，单位为byte，但是这个大小不是精确的；bufsize=负数，表示使用一个系统默认大小的缓冲，对于tty字元设备一般是行缓冲，而对于其他文件则一般是全缓冲。如果这个参数没有制定，则使用系统默认的缓冲设定。
    

### 返回值

通过文件描述符返回的文件对象。

### 实例

以下实例演示了 fdopen() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 打开文件
fd = os.open( "foo.txt", os.O\_RDWR|os.O\_CREAT )

\# 获取以上文件的对象
fo = os.fdopen(fd, "w+")

\# 获取当前文章
print "Current I/O pointer position :%d" % fo.tell()

\# 写入字符串
fo.write( "Python is a great language.\\nYeah its great!!\\n");

\# 读取内容
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print "Read String is : ", str

\# 获取当前位置
print "Current I/O pointer position :%d" % fo.tell()

\# 关闭文件
os.close( fd )

print "关闭文件成功!!"
```
执行以上程序输出结果为：
```
Current I/O pointer position :0
Read String is :  This is testPython is a great language.
Yeah its great!!

Current I/O pointer position :45
关闭文件成功!!
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)