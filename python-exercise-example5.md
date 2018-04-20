Python 练习实例5
============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**输入三个整数x,y,z，请把这三个数由小到大输出。

**程序分析：**我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。

程序源代码：

实例
--
```
#!/usr/bin/python  
\# -*- coding: UTF-8 -*-  l = \[\]  
for  i  in  range(3): x = int(raw_input('integer:\\n'))
l.append(x)  
l.sort()  
print  l
```
以上实例输出结果为：
```
integer:  8 integer:  5 integer:  6  \[5,  6,  8\]
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)