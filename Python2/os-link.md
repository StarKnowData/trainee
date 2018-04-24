Python os.link() 方法
===================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.link() 方法用于创建硬链接，名为参数 dst，指向参数 src。

该方法对于创建一个已存在文件的拷贝是非常有用的。

只支持在 Unix, Windows 下使用。

### 语法

**link()**方法语法格式如下：
```
os.link(src, dst)
```
### 参数

*   **src** \-\- 用于创建硬连接的源地址
    
*   **dst** \-\- 用于创建硬连接的目标地址
    

### 返回值

该方法没有返回值。

### 实例

以下实例演示了 link() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 打开文件
path = "/var/www/html/foo.txt"
fd = os.open( path, os.O\_RDWR|os.O\_CREAT )

\# 关闭文件
os.close( fd )

\# 创建以上文件的拷贝
dst = "/tmp/foo.txt"
os.link( path, dst)

print "创建硬链接成功!!"
```
执行以上程序输出结果为：
```
创建硬链接成功!!
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)