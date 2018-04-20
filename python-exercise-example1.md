Python 练习实例1
============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

**程序分析：**可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。

程序源代码：

实例(Python 2.0+)
---------------
```
#!/usr/bin/python 
\# -*- coding: UTF-8 -*- 

for  i  in  range(1,5): 
for  j  in  range(1,5): 
for  k  in  range(1,5):
if(  i != k  )  and  (i != j)  and  (j != k):
print  i,j,k
```
以上实例输出结果为：
```
1 2 3
1 2 4
1 3 2
1 3 4
1 4 2
1 4 3
2 1 3
2 1 4
2 3 1
2 3 4
2 4 1
2 4 3
3 1 2
3 1 4
3 2 1
3 2 4
3 4 1
3 4 2
4 1 2
4 1 3
4 2 1
4 2 3
4 3 1
4 3 2
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)