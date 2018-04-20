Python os.tmpfile() 方法
======================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.tmpfile() 方法用于返回一个打开的模式为(w+b)的临时文件对象，这文件对象没有文件夹入口，没有文件描述符，将会自动删除。

### 语法

**tmpfile()**方法语法格式如下：
```
os.tmpfile
```
### 参数

*   无
    

### 返回值

返回一个临时文件对象。

### 实例

以下实例演示了 tmpfile() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os

\# 创建临时文件对象
tmpfile = os.tmpfile()
tmpfile.write('临时文件在这创建了.....')
tmpfile.seek(0)

print tmpfile.read()
tmpfile.close
```
执行以上程序输出结果为：
```
临时文件在这创建了.....
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)