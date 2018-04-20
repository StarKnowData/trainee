Python os.walk() 方法
===================

 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)

* * *

### 概述

os.walk() 方法用于通过在目录树中游走输出在目录中的文件名，向上或者向下。

os.walk() 方法是一个简单易用的文件、目录遍历器，可以帮助我们高效的处理文件、目录方面的事情。

在Unix，Windows中有效。

### 语法

**walk()**方法语法格式如下：
```
os.walk(top[, topdown=True[, onerror=None[, followlinks=False]]])
```
### 参数

*   **top** \-\- 是你所要便利的目录的地址, 返回的是一个三元组(root,dirs,files)。
    
    *   root 所指的是当前正在遍历的这个文件夹的本身的地址
    *   dirs 是一个 list ，内容是该文件夹中所有的目录的名字(不包括子目录)
    *   files 同样是 list , 内容是该文件夹中所有的文件(不包括子目录)
*   **topdown** --可选，为 True，则优先遍历 top 目录，否则优先遍历 top 的子目录(默认为开启)。如果 topdown 参数为 True，walk 会遍历top文件夹，与top 文件夹中每一个子目录。
    
*   **onerror** \-\- 可选， 需要一个 callable 对象，当 walk 需要异常时，会调用。
    
*   **followlinks** \-\- 可选， 如果为 True，则会遍历目录下的快捷方式(linux 下是 symbolic link)实际所指的目录(默认关闭)。
    

### 返回值

该方法没有返回值。

### 实例

以下实例演示了 walk() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

import os
for root, dirs, files in os.walk(".", topdown=False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
```
执行以上程序输出结果为：
```
./.bash_logout
./amrood.tar.gz
./.emacs
./httpd.conf
./www.tar.gz
./mysql.tar.gz
./test.py
./.bashrc
./.bash_history
./.bash_profile
./tmp
./tmp/test.py
```
 [![Python File(文件) 方法](../images/up.gif) Python OS 文件/目录方法](os-file-methods.html)```