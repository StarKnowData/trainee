Python 练习实例79
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**字符串排序。

**程序分析：**无。
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  if  \_\_name\_\_ == '\_\_main\_\_': str1 = raw_input('input string:\\n')  str2 = raw_input('input string:\\n')  str3 = raw_input('input string:\\n')  print  str1,str2,str3  if  str1 \> str2 : str1,str2 = str2,str1  if  str1 \> str3 : str1,str3 = str3,str1  if  str2 \> str3 : str2,str3 = str3,str2  print  'after being sorted.'  print  str1,str2,str3
```
以上实例输出结果为：
```
input string:
abcde
input string:
efdis
input string:
adk
abcde efdis adk
after being sorted.
abcde adk efdis
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)