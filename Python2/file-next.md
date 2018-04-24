Python File next() 方法
=====================

 [![Python File(文件) 方法](../images/up.gif) Python File(文件) 方法](file-methods.html)

* * *

### 概述

**next()** 方法在文件使用迭代器时会使用到，在循环中，next()方法会在每次循环中调用，该方法返回文件的下一行，如果到达结尾(EOF),则触发 _StopIteration_

### 语法

next() 方法语法如下：
```
fileObject.next(); 
```
### 参数

*   **无**
    

### 返回值

返回文件下一行。

### 实例

以下实例演示了 next() 方法的使用：

文件 runoob.txt 的内容如下：
```
这是第一行
这是第二行
这是第三行
这是第四行
这是第五行
```
循环读取文件的内容：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

\# 打开文件
fo = open("runoob.txt", "rw+")
print "文件名为: ", fo.name

for index in range(5):
    line = fo.next()
    print "第 %d 行 - %s" % (index, line)

\# 关闭文件
fo.close()
```
以上实例输出结果为：
```
文件名为:  runoob.txt
第 0 行 - 这是第一行

第 1 行 - 这是第二行

第 2 行 - 这是第三行

第 3 行 - 这是第四行

第 4 行 - 这是第五行
```
 [![Python File(文件) 方法](../images/up.gif) Python File(文件) 方法](file-methods.html)