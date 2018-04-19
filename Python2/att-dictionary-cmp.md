Python 字典(Dictionary) cmp()方法

描述

Python 字典的 cmp() 函数用于比较两个字典元素。

语法

cmp()方法语法：

cmp(dict1, dict2)
参数

dict1 -- 比较的字典。
dict2 -- 比较的字典。
返回值

如果两个字典的元素相同返回0，如果字典dict1大于字典dict2返回1，如果字典dict1小于字典dict2返回-1。

实例

以下实例展示了 cmp()函数的使用方法：

实例(Python 2.0+)

#!/usr/bin/python  
\# -*- coding: UTF-8 -*- 

dict1 = {'Name': 'Zara', 'Age': 7}  
dict2 = {'Name': 'Mahnaz', 'Age': 27}  
dict3 = {'Name': 'Abid', 'Age': 27}  
dict4 = {'Name': 'Zara', 'Age': 7}  
print  "Return Value : %d" % cmp  (dict1, dict2)  
print  "Return Value : %d" % cmp  (dict2, dict3)   
print  "Return Value : %d" % cmp  (dict1, dict4)    
以上实例输出结果为：

Return  Value  :  -1  
Return  Value  :  1  
Return  Value  :  0
