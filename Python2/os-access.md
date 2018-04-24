Python os.access() 方法
=====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.access() 方法使用当前的uid/gid尝试访问路径。大部分操作使用有效的 uid/gid, 因此运行环境可以在 suid/sgid 环境尝试。

### 语法

**access()**方法语法格式如下：
```
os.access(path, mode);
```
### 参数

*   **path** \-\- 要用来检测是否有访问权限的路径。
    
*   **mode** \-\- mode为F\_OK，测试存在的路径，或者它可以是包含R\_OK, W\_OK和X\_OK或者R\_OK, W\_OK和X_OK其中之一或者更多。
    
    *   **os.F_OK:** 作为access()的mode参数，测试path是否存在。
    *   **os.R_OK:** 包含在access()的mode参数中 ， 测试path是否可读。
    *   **os.W_OK** 包含在access()的mode参数中 ， 测试path是否可写。
    *   **os.X_OK** 包含在access()的mode参数中 ，测试path是否可执行。

### 返回值

如果允许访问返回 True , 否则返回False。

### 实例

以下实例演示了 access() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 假定 /tmp/foo.txt 文件存在，并有读写权限

ret = os.access("/tmp/foo.txt", os.F_OK)
print "F_OK - 返回值 %s"% ret

ret = os.access("/tmp/foo.txt", os.R_OK)
print "R_OK - 返回值 %s"% ret

ret = os.access("/tmp/foo.txt", os.W_OK)
print "W_OK - 返回值 %s"% ret

ret = os.access("/tmp/foo.txt", os.X_OK)
print "X_OK - 返回值 %s"% ret
```
执行以上程序输出结果为：
```
F_OK - 返回值 True
R_OK - 返回值 True
W_OK - 返回值 True
X_OK - 返回值 False
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)