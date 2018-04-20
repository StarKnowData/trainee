Python 练习实例39
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

**程序分析：**首先判断此数是否大于最后一个数，然后再考虑插入中间的数的情况，插入后此元素之后的数，依次后移一个位置。

程序源代码：

实例(Python 2.0+)
---------------
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  if  \_\_name\_\_ == '\_\_main\_\_': \# 方法一 ： 0 作为加入数字的占位符  a = \[1,4,6,9,13,16,19,28,40,100,0\]  print  '原始列表:'  for  i  in  range(len(a)): print  a\[i\], number = int(raw_input("\\n插入一个数字:\\n"))  end = a\[9\]  if  number \> end: a\[10\] = number  else: for  i  in  range(10): if  a\[i\] \> number: temp1 = a\[i\]  a\[i\] = number  for  j  in  range(i \+ 1,11): temp2 = a\[j\]  a\[j\] = temp1  temp1 = temp2  break  print  '排序后列表:'  for  i  in  range(11): print  a\[i\],
```
以上实例输出结果为：
```
原始列表:
1 4 6 9 13 16 19 28 40 100 0 
插入一个数字:
7
排序后列表:
1 4 6 7 9 13 16 19 28 40 100
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)