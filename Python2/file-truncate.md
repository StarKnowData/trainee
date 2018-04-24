Python File truncate() 方法
=========================

 [![Python File(文件) 方法](../images/up.gif) Python File(文件) 方法](file-methods.html)

* * *

### 概述

**truncate()** 方法用于截断文件，如果指定了可选参数 size，则表示截断文件为 size 个字符。 如果没有指定 size，则从当前位置起截断；截断之后 size 后面的所有字符被删除。

### 语法

truncate() 方法语法如下：
```
fileObject.truncate( [ size ])
```
### 参数

*   **size** \-\- 可选，如果存在则文件截断为 size 字节。
    

### 返回值

该方法没有返回值。

### 实例

以下实例演示了 truncate() 方法的使用：

文件 runoob.txt 的内容如下：
```
1:www.runoob.com
2:www.runoob.com
3:www.runoob.com
4:www.runoob.com
5:www.runoob.com
```
循环读取文件的内容：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

\# 打开文件
fo = open("runoob.txt", "r+")
print "文件名为: ", fo.name

line = fo.readline()
print "读取第一行: %s" % (line)

\# 截断剩下的字符串
fo.truncate()

\# 尝试再次读取数据
line = fo.readline()
print "读取数据: %s" % (line)

\# 关闭文件
fo.close()
```
以上实例输出结果为：
```
文件名为:  runoob.txt
读取第一行: 1:www.runoob.com
```
读取数据:

以下实例截取 runoob.txt 文件的10个字节：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

\# 打开文件
fo = open("runoob.txt", "r+")
print "文件名为: ", fo.name

\# 截取10个字节
fo.truncate(10)

str = fo.read()
print "读取数据: %s" % (str)

\# 关闭文件
fo.close()
```
以上实例输出结果为：
```
文件名为:  runoob.txt
读取数据: 1:www.runo
```
 [![Python File(文件) 方法](../images/up.gif) Python File(文件) 方法](file-methods.html)