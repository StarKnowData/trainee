Python os.chown() 方法
====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.chown() 方法用于更改文件所有者，如果不修改可以设置为 -1, 你需要超级用户权限来执行权限修改操作。

只支持在 Unix 下使用。

### 语法

**chown()**方法语法格式如下：
```
os.chown(path, uid, gid);
```
### 参数

*   **path** \-\- 设置权限的文件路径
    
*   **uid** \-\- 所属用户 ID
    
*   **gid** \-\- 所属用户组 ID
    

### 返回值

该方法没有返回值。

### 实例

以下实例演示了 lchmod() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 假定 /tmp/foo.txt 文件存在.
\# 设置所有者 ID 为 100 
os.chown("/tmp/foo.txt", 100, -1)

print "修改权限成功!!"
```
执行以上程序输出结果为：
```
修改权限成功!!
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)