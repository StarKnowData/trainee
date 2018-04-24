Python 练习实例89
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。

**程序分析：**无。

程序源代码：

实例
--
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  from  sys  import  stdout  if  \_\_name\_\_ == '\_\_main\_\_': a = int(raw_input('输入四个数字:\\n'))  aa = \[\]  aa.append(a % 10)  aa.append(a % 100 / 10)  aa.append(a % 1000 / 100)  aa.append(a / 1000)  for  i  in  range(4): aa\[i\] += 5  aa\[i\] %= 10  for  i  in  range(2): aa\[i\],aa\[3 \- i\] = aa\[3 \- i\],aa\[i\]  for  i  in  range(3,-1,-1): stdout.write(str(aa\[i\]))
```
以上实例输出结果为：
```
输入四个数字:  1234  9876
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)