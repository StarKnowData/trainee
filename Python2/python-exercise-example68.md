Python 练习实例68
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

**程序分析：**无。

程序源代码：

实例
--
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  if  \_\_name\_\_ == '\_\_main\_\_': n = int(raw_input('整数 n 为:\\n'))  m = int(raw_input('向后移 m 个位置为:\\n'))  def  move(array,n,m): array_end = array\[n \- 1\]  for  i  in  range(n \- 1,-1,\- 1): array\[i\] = array\[i \- 1\]  array\[0\] = array_end  m -= 1  if  m \> 0:move(array,n,m)  number = \[\]  for  i  in  range(n): number.append(int(raw_input('输入一个数字:\\n')))  print  '原始列表:',number  move(number,n,m)  print  '移动之后:',number
```
以上实例输出结果为：
```
整数 n 为:
8
向后移 m 个位置为:
5
输入一个数字:
2
输入一个数字:
8
输入一个数字:
6
输入一个数字:
1
输入一个数字:
78
输入一个数字:
45
输入一个数字:
34
输入一个数字:
2
原始列表: \[2, 8, 6, 1, 78, 45, 34, 2\]
移动之后: \[1, 78, 45, 34, 2, 2, 8, 6\]
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)