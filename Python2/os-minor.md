Python os.minor() 方法
====================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.minor() 方法用于从原始的设备号中提取设备minor号码 (使用stat中的st\_dev或者st\_rdev field )。

### 语法

**minor()**方法语法格式如下：
```
os.minor(device)
```
### 参数

*   **device** \-\- 原始的设备(使用stat中的st\_dev或者st\_rdev field )
    

### 返回值

返回设备 minor 号。

### 实例

以下实例演示了 minor() 方法的使用：
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  import os, sys

path =  "/var/www/html/foo.txt"  \# 获取元组 info = os.lstat(path)  \# 获取 major 和 minor 设备号 major_dnum = os.major(info.st_dev) minor_dnum = os.minor(info.st_dev)  print  "Major 设备号 :", major_dnum print  "Minor 设备号 :", minor_dnum 
```
执行以上程序输出结果为：
```
Major  设备号  :  0  Minor  设备号  :  103
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)