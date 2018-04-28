Python File write() 方法
======================

 [![Python File(文件) 方法](../images/up.gif)
 Python File(文件) 方法](file-methods.html)


  ### 概述

 **write()** 方法用于向文件中写入指定字符串。

 在文件关闭前或缓冲区刷新前，字符串内容存储在缓冲区中，这时你在文件中是看不到写入的内容的。

 ### 语法

 write() 方法语法如下：

 
```

fileObject.write( [ str ])

```

 ### 参数

  *  **str** -- 要写入文件的字符串。 

 
  ### 返回值

 该方法没有返回值。

 ### 实例

 以下实例演示了 write() 方法的使用：

 
```

#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开文件
fo = open("test.txt", "w")
print "文件名为: ", fo.name
str = "菜鸟教程"
fo.write( str )

# 关闭文件
fo.close()

```

 以上实例输出结果为：

 
```

文件名为:  test.txt

```

 查看文件内容：

 
```

$ cat test.txt 
菜鸟教程

```

 [![Python File(文件) 方法](../images/up.gif)
 Python File(文件) 方法](file-methods.html)


