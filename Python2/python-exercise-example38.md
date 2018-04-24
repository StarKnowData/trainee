Python 练习实例38
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**求一个3*3矩阵主对角线元素之和。

**程序分析：**利用双重for循环控制输入二维数组，再将a\[i\]\[i\]累加后输出。

程序源代码：

实例
--
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  if  \_\_name\_\_ == '\_\_main\_\_': a = \[\]  sum = 0.0  for  i  in  range(3): a.append(\[\])  for  j  in  range(3): a\[i\].append(float(raw_input("input num:\\n")))  for  i  in  range(3): sum += a\[i\]\[i\]  print  sum
```
以上实例输出结果为：
```
input num:
78
input num:
34
input num:
23
input num:
34
input num:
56
input num:
33
input num:
12
input num:
21
input num:
2
136.0
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)