Python os.dup2() 方法
===================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.dup2() 方法用于将一个文件描述符 fd 复制到另一个 fd2。

Unix, Windows 上可用。

### 语法

**dup2()**方法语法格式如下：
```
os.dup2(fd, fd2);
```
### 参数

*   **fd** \-\- 要被复制的文件描述符
    
*   **fd2** \-\- 复制的文件描述符
    

### 返回值

没有返回值。

### 实例

以下实例演示了 dup2() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 打开文件
fd = os.open( "foo.txt", os.O\_RDWR|os.O\_CREAT )

\# 写入字符串
os.write(fd, "This is test")

\# 文件描述符为 1000
fd2 = 1000
os.dup2(fd, fd2);

\# 在新的文件描述符上插入数据
os.lseek(fd2, 0, 0)
str = os.read(fd2, 100)
print "读取的字符串是 : ", str

\# 关闭文件
os.close( fd )

print "关闭文件成功!!"
```
执行以上程序输出结果为：
```
读取的字符串是 :  This is test
关闭文件成功!!
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)