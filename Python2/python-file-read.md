Python File read() 方法
=====================

 [![Python File(文件) 方法](../images/up.gif) Python File(文件) 方法](file-methods.html)

* * *

### 概述

**read()** 方法用于从文件读取指定的字节数，如果未给定或为负则读取所有。

### 语法

read() 方法语法如下：

fileObject.read(); 

### 参数

*   **size** \-\- 从文件中读取的字节数。
    

### 返回值

返回从字符串中读取的字节。

### 实例

以下实例演示了 read() 方法的使用：

文件 runoob.txt 的内容如下：

1:www.runoob.com
2:www.runoob.com
3:www.runoob.com
4:www.runoob.com
5:www.runoob.com

循环读取文件的内容：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

\# 打开文件
fo = open("runoob.txt", "rw+")
print "文件名为: ", fo.name

line = fo.read(10)
print "读取的字符串: %s" % (line)

\# 关闭文件
fo.close()
```
以上实例输出结果为：
```
文件名为:  runoob.txt
读取的字符串: 1:www.runo
```
 [![Python File(文件) 方法](../images/up.gif) Python File(文件) 方法](file-methods.html)