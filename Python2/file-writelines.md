Python File writelines() 方法
===========================

 [![Python File(文件) 方法](../images/up.gif) Python File(文件) 方法](file-methods.html)

* * *

### 概述

**writelines()** 方法用于向文件中写入一序列的字符串。

这一序列字符串可以是由迭代对象产生的，如一个字符串列表。

换行需要制定换行符 \\n。

### 语法

writelines() 方法语法如下：
```
fileObject.writelines( [ str ])
```
### 参数

*   **str** \-\- 要写入文件的字符串序列。
    

### 返回值

该方法没有返回值。

### 实例

以下实例演示了 writelines() 方法的使用：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

\# 打开文件
fo = open("test.txt", "w")
print "文件名为: ", fo.name
seq = ["菜鸟教程 1\n", "菜鸟教程 2"\]
fo.writelines( seq )

\# 关闭文件
fo.close()
```
以上实例输出结果为：
```
文件名为:  test.txt

查看文件内容：

$ cat test.txt 
菜鸟教程 1
菜鸟教程 2
```
 [![Python File(文件) 方法](../images/up.gif) Python File(文件) 方法](file-methods.html)