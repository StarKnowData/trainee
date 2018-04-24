Python 练习实例37
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**对10个数进行排序。

**程序分析：**可以利用选择法，即从后9个比较过程中，选择一个最小的与第一个元素交换，下次类推，即用第二个元素与后8个进行比较，并进行交换。

程序源代码：
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  if  \_\_name\_\_ == "\_\_main\_\_": N = 10  \# input data  print  '请输入10个数字:\\n'  l = \[\]  for  i  in  range(N): l.append(int(raw_input('输入一个数字:\\n')))  print  for  i  in  range(N): print  l\[i\]  print  \# 排列10个数字  for  i  in  range(N \- 1): min = i  for  j  in  range(i \+ 1,N): if  l\[min\] \> l\[j\]:min = j  l\[i\],l\[min\] = l\[min\],l\[i\]  print  '排列之后：'  for  i  in  range(N): print  l\[i\]
```
以上实例输出结果为：
```
请输入10个数字:

输入一个数字:
5
输入一个数字:
3
输入一个数字:
23
输入一个数字:
67
输入一个数字:
2
输入一个数字:
56
输入一个数字:
45
输入一个数字:
98
输入一个数字:
239
输入一个数字:
9

5
3
23
67
2
56
45
98
239
9

排列之后：
2
3
5
9
23
45
56
67
98
239
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)