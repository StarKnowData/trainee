Python os.lchown() 方法
=====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.lchown() 方法用于更改文件所有者，类似 chown，但是不追踪链接。

只支持在 Unix 下使用。

### 语法

**lchown()**方法语法格式如下：
```
os.lchown(path, uid, gid)
```
### 参数

*   **path** \-\- 设置权限的文件路径
    
*   **uid** \-\- 所属用户 ID
    
*   **gid** \-\- 所属用户组 ID
    

### 返回值

该方法没有返回值。

### 实例

以下实例演示了 lchown() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 打开文件
path = "/var/www/html/foo.txt"
fd = os.open( path, os.O\_RDWR|os.O\_CREAT )

\# 关闭打开的文件
os.close( fd )

\# 修改文件权限
\# 设置文件所属用户 ID
os.lchown( path, 500, -1)

\# 设置文件所属用户组 ID
os.lchown( path, -1, 500)

print "修改权限成功!!"
```
执行以上程序输出结果为：
```
修改权限成功!!
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)