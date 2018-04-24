Python os.pathconf() 方法
=======================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.pathconf() 方法用于返回一个打开的文件的系统配置信息。

Unix 平台下可用。

### 语法

**fpathconf()**方法语法格式如下：
```
os.fpathconf(fd, name)
```
### 参数

*   **name** \-\- 文件描述符
    

*   **name** \-\- 检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。一些平台也定义了一些额外的名字。这些名字在主操作系统上pathconf\_names的字典中。对于不在pathconf\_names中的配置变量，传递一个数字作为名字，也是可以接受的。
    

### 返回值

返回文件的系统信息。

### 实例

以下实例演示了 fpathconf() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 打开文件
fd = os.open( "foo.txt", os.O\_RDWR|os.O\_CREAT )

print "%s" % os.pathconf_names

\# 获取文件最大连接数
no = os.fpathconf(fd, 'PC\_LINK\_MAX')
print "Maximum number of links to the file. :%d" % no

\# 获取文件名最大长度
no = os.fpathconf(fd, 'PC\_NAME\_MAX')
print "Maximum length of a filename :%d" % no

\# 关闭文件
os.close( fd)

print "关闭文件成功!!"
```
执行以上程序输出结果为：
```
关闭文件成功!!
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)