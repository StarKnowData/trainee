Python File flush() 方法
======================

 [![Python File(文件) 方法](../images/up.gif) Python File(文件) 方法](file-methods.html)

* * *

### 概述

**flush()** 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，同时清空缓冲区，不需要是被动的等待输出缓冲区写入。

一般情况下，文件关闭后会自动刷新缓冲区，但有时你需要在关闭前刷新它，这时就可以使用 flush() 方法。

### 语法

flush() 方法语法如下：
```
fileObject.flush();
```
### 参数

*   **无**
    

### 返回值

该方法没有返回值。

### 实例

以下实例演示了 flush() 方法的使用：

实例
--
```
#!/usr/bin/python  
\# -*- coding: UTF-8 -*-

\# 打开文件  
fo = open("runoob.txt", "wb")   
print  "文件名为: ", fo.name

\# 刷新缓冲区    
fo.flush()  

\# 关闭文件   
fo.close()
```
以上实例输出结果为：
```
文件名为:  runoob.txt
```
 [![Python File(文件) 方法](../images/up.gif) Python File(文件) 方法](file-methods.html)