Python os.tempnam() 方法
======================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.tempnam() 方法用于返回唯一的路径名用于创建临时文件。

### 语法

**tempnam()**方法语法格式如下：
```
os.tempnam(dir, prefix)
```
### 参数

*   **dir** \-\- 要创建的临时文件路径。
    
*   **prefix** \-\- 临时文件前缀
    

### 返回值

该方法返回唯一路径。

### 实例

以下实例演示了 tempnam() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 前缀为 runoob 的文件
tmpfn = os.tempnam('/tmp/runoob,'runoob')

print "这是一个唯一路径:"
print tmpfn
```
执行以上程序输出结果为：
```
这是一个唯一路径:
/tmp/runoob/runoobIbAco8
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)