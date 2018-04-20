Python os.write() 方法
====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.write() 方法用于写入字符串到文件描述符 fd 中. 返回实际写入的字符串长度。

在Unix中有效。

### 语法

**write()**方法语法格式如下：
```
os.write(fd, str)
```
### 参数

*   **fd** \-\- 文件描述符。
    
*   **str** \-\- 写入的字符串。
    

### 返回值

该方法返回写入的实际位数。

### 实例

以下实例演示了 write() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 打开文件
fd = os.open("f1.txt",os.O\_RDWR|os.O\_CREAT)

\# 写入字符串
ret = os.write(fd,"This is runoob.com site")

\# 输入返回值
print "写入的位数为: "
print  ret

print "写入成功"

\# 关闭文件
os.close(fd)
print "关闭文件成功!!"
```
执行以上程序输出结果为：
```
写入的位数为: 
23
写入成功
关闭文件成功!!
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)