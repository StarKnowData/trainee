Python File seek() 方法
=====================

 [![Python File(文件) 方法](../images/up.gif) Python File(文件) 方法](file-methods.html)

* * *

### 概述

**seek()** 方法用于移动文件读取指针到指定位置。

### 语法

seek() 方法语法如下：
```
fileObject.seek(offset[, whence])
```
### 参数

*   **offset** \-\- 开始的偏移量，也就是代表需要移动偏移的字节数
    
*   **whence：**可选，默认值为 0。给offset参数一个定义，表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
    

### 返回值

该函数没有返回值。

### 实例

以下实例演示了 readline() 方法的使用：

文件 runoob.txt 的内容如下：
```
1:www.runoob.com 2:www.runoob.com 3:www.runoob.com 4:www.runoob.com 5:www.runoob.com
```
循环读取文件的内容：
```
#!/usr/bin/python   
\# -*- coding: UTF-8 -*-  

\# 打开文件  
fo = open("runoob.txt",  "rw+")  print  "文件名为: ", fo.name

line = fo.readline()   
print  "读取的数据为: %s"  %  (line)  \# 重新设置文件读取指针到开头 fo.seek(0,  0) line = fo.readline()  
print  "读取的数据为: %s"  %  (line)  

\# 关闭文件  
fo.close()
```
以上实例输出结果为：
```
文件名为: runoob.txt   
读取的数据为:  1:www.runoob.com  
读取的数据为:  1:www.runoob.com
```
 [![Python File(文件) 方法](../images/up.gif) Python File(文件) 方法](file-methods.html)