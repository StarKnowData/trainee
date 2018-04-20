Python os.isatty() 方法
=====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.isatty() 方法用于判断如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。

### 语法

**isatty()**方法语法格式如下：
```
os.isatty()
```
### 参数

*   无

### 返回值

如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。

### 实例

以下实例演示了 isatty() 方法的使用：
```
#!/usr/bin/python   
\# -*- coding: UTF-8 -*- 

import os, sys
\# 打开文件 
fd = os.open(  "foo.txt", os.O_RDWR|os.O_CREAT ) 
\# 写入字符串 
os.write(fd,  "This is test") 
\# 使用 isatty() 查看文件 
ret = os.isatty(fd) 

print  "返回值: ", ret \# 关闭文件 os.close( fd )
```
执行以上程序输出结果为：
```
返回值:  False
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)