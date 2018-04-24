Python 练习实例90
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**列表使用实例。

**程序分析：**无。
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  #list #新建列表 testList=\[10086,'中国移动',\[1,2,4,5\]\]  #访问列表长度 print  len(testList)  #到列表结尾 print  testList\[1:\]  #向列表添加元素 testList.append('i\\'m new here!')  print  len(testList)  print  testList\[-1\]  #弹出列表的最后一个元素 print  testList.pop(1)  print  len(testList)  print  testList  #list comprehension #后面有介绍，暂时掠过 matrix = \[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\]\]  print  matrix  print  matrix\[1\]  col2 = \[row\[1\]  for  row  in  matrix\]#get a column from a matrix print  col2  col2even = \[row\[1\]  for  row  in  matrix  if  row\[1\] % 2 == 0\]#filter odd item print  col2even
```
以上实例输出结果为：
```
3
\['\\xe4\\xb8\\xad\\xe5\\x9b\\xbd\\xe7\\xa7\\xbb\\xe5\\x8a\\xa8', \[1, 2, 4, 5\]\]
4
i'm new here!
中国移动
3
\[10086, \[1, 2, 4, 5\], "i'm new here!"\]
\[\[1, 2, 3\], \[4, 5, 6\], \[7, 8, 9\]\]
\[4, 5, 6\]
\[2, 5, 8\]
\[2, 8\]
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)