Python - 获取 100 以内的质数
=====================

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

题目： 获取 100 以内的质数。

**程序分析：**质数（prime number）又称素数，有无限个。质数定义为在大于1的自然数中，除了1和它本身以外不再有其他因数的数称为质数，如：2、3、5、7、11、13、17、19。
```
方法一：
----

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  num=\[\]; i=2  for  i  in  range(2,100): j=2  for  j  in  range(2,i): if(i%j==0): break  else: num.append(i)  print(num)

方法二：
----

import  math  def  func\_get\_prime(n): return  filter(lambda  x: not  \[x%i  for  i  in  range(2, int(math.sqrt(x))+1)  if  x%i ==0\], range(2,n+1))  print  func\_get\_prime(100)
```
输出结果为：
```
\[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97\]
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)