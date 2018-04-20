Python os.lseek() 方法
====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.lseek() 方法用于设置文件描述符 fd 当前位置为 pos, how 方式修改。

在Unix，Windows中有效。

### 语法

**lseek()**方法语法格式如下：
```
os.lseek(fd, pos, how)
```
### 参数

*   **fd** \-\- 文件描述符。
    
*   **pos** \-\- 这是相对于给定的参数 how 在文件中的位置。。
    
*   **how** \-\- 文件内参考位置。SEEK\_SET 或者 0 设置从文件开始的计算的pos; SEEK\_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始。
    

### 返回值

该方法没有返回值。

### 实例

以下实例演示了 lseek() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 打开文件
fd = os.open( "foo.txt", os.O\_RDWR|os.O\_CREAT )

\# 写入字符串
os.write(fd, "This is test")

\# 所有 fsync() 方法
os.fsync(fd)

\# 从开始位置读取字符串
os.lseek(fd, 0, 0)
str = os.read(fd, 100)
print "Read String is : ", str

\# 关闭文件
os.close( fd )

print "关闭文件成功!!"
```
执行以上程序输出结果为：
```
关闭文件成功!!
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)