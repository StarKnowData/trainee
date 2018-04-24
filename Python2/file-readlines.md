Python File readlines() 方法
==========================

 [![Python File(文件) 方法](../images/up.gif) Python File(文件) 方法](file-methods.html)

* * *

### 概述

**readlines()** 方法用于读取所有行(直到结束符 EOF)并返回列表，该列表可以由 Python 的 for... in ... 结构进行处理。

如果碰到结束符 EOF 则返回空字符串。

### 语法

readlines() 方法语法如下：
```
fileObject.readlines( );
```
### 参数

*   无。
    

### 返回值

返回列表，包含所有的行。

### 实例

以下实例演示了 readline() 方法的使用：

文件 runoob.txt 的内容如下：
```
1:www.runoob.com
2:www.runoob.com
3:www.runoob.com
4:www.runoob.com
5:www.runoob.com
```
循环读取文件的内容：

实例
--
```
#!/usr/bin/python    
\# -*- coding: UTF-8 -*- 

\# 打开文件   
fo = open("runoob.txt", "r")    
print  "文件名为: ", fo.name   
for  line  in  fo.readlines(): #依次读取每行 line = line.strip()  #去掉每行头尾空白   
print  "读取的数据为: %s" % (line) 

\# 关闭文件   
fo.close()
```
以上实例输出结果为：
```
文件名为:  runoob.txt
读取的数据为: 1:www.runoob.com
读取的数据为: 2:www.runoob.com
读取的数据为: 3:www.runoob.com
读取的数据为: 4:www.runoob.com
读取的数据为: 5:www.runoob.com
```
 [![Python File(文件) 方法](../images/up.gif) Python File(文件) 方法](file-methods.html)