Python os.rename() 方法
=====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.rename() 方法用于命名文件或目录，从 src 到 dst,如果dst是一个存在的目录, 将抛出OSError。

### 语法

**rename()**方法语法格式如下：
```
os.rename(src, dst)
```
### 参数

*   **src** \-\- 要修改的目录名
    
*   **dst** \-\- 修改后的目录名
    

### 返回值

该方法没有返回值

### 实例

以下实例演示了 rename() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os, sys

\# 列出目录
print "目录为: %s"%os.listdir(os.getcwd())

\# 重命名
os.rename("test","test2")

print "重命名成功。"

\# 列出重命名后的目录
print "目录为: %s" %os.listdir(os.getcwd())
```
执行以上程序输出结果为：
```
目录为:
\[  'a1.txt','resume.doc','a3.py','test' \]
重命名成功。
\[  'a1.txt','resume.doc','a3.py','test2' \]
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)