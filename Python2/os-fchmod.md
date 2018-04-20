Python os.fchmod() 方法
=====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.fchmod() 方法用于改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。

Unix上可用。

### 语法

**fchmod()**方法语法格式如下：
```
os.fchmod(fd, mode);
```
### 参数

*   **fd** \-\- 文件描述符
    
*   **mode** \-\- 可以是以下一个或多个组成，多个使用 "|" 隔开：
    
    *   **stat.S_ISUID:**设置 UID 位
        
    *   **stat.S_ISGID:** 设置组 ID 位
        
    *   **stat.S_ENFMT:** 系统文件锁定的执法行动
        
    *   **stat.S_ISVTX:** 在执行之后保存文字和图片
        
    *   **stat.S_IREAD:** 对于拥有者读的权限
        
    *   **stat.S_IWRITE:** 对于拥有者写的权限
        
    *   **stat.S_IEXEC:** 对于拥有者执行的权限
        
    *   **stat.S_IRWXU:**对于拥有者读、写、执行的权限
        
    *   **stat.S_IRUSR:** 对于拥有者读的权限
        
    *   **stat.S_IWUSR:** 对于拥有者写的权限
        
    *   **stat.S_IXUSR:** 对于拥有者执行的权限
        
    *   **stat.S_IRWXG:** 对于同组的人读写执行的权限
        
    *   **stat.S_IRGRP:** 对于同组读的权限
        
    *   **stat.S_IWGRP:**对于同组写的权限
        
    *   **stat.S_IXGRP:** 对于同组执行的权限
        
    *   **stat.S_IRWXO:** 对于其他组读写执行的权限
        
    *   **stat.S_IROTH:** 对于其他组读的权限
        
    *   **stat.S_IWOTH:** 对于其他组写的权限
        
    *   **stat.S_IXOTH:**对于其他组执行的权限
        

### 返回值

该方法没有返回值。

### 实例

以下实例演示了 fchmod() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys, stat

\# 打开文件 "/tmp/foo.txt"
fd = os.open( "/tmp", os.O_RDONLY )

\# 设置文件可通过组执行

os.fchmod( fd, stat.S_IXGRP)

\# 设置文件可被其他用户写入
os.fchmod(fd, stat.S_IWOTH)

print "修改权限成功!!"

\# 关闭文件
os.close( fd )
```
执行以上程序输出结果为：
```
修改权限成功!!
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)