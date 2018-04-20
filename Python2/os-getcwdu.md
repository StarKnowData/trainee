Python os.getcwdu() 方法
======================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.getcwdu() 方法用于返回一个当前工作目录的Unicode对象。

Unix, Windows 系统下可用。

### 语法

**getcwdu()**方法语法格式如下：
```
os.getcwdu()
```
### 参数

*   无

### 返回值

返回一个当前工作目录的Unicode对象。

### 实例

以下实例演示了 getcwdu() 方法的使用：
```
#!/usr/bin/python    
\# -*- coding: UTF-8 -*- 

import os, sys   
\# 切换到 "/var/www/html" 目录 os.chdir("/var/www/html"  )    
\# 打印当前目录  
print  "当前工作目录 : %s"  % os.getcwdu()   
\# 打开 "/tmp"   
fd = os.open(  "/tmp", os.O_RDONLY )   
\# 使用 os.fchdir()方法修改目录   
os.fchdir(fd)  \# 打印当前目录    
print  "当前工作目录 : %s"  % os.getcwdu()    
\# 关闭文件
os.close( fd )
```
执行以上程序输出结果为：
```
当前工作目录  :  /var/www/html 当前工作目录  :  /tmp
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)