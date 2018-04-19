Python 字典(Dictionary) fromkeys()方法

描述

Python 字典(Dictionary) fromkeys() 函数用于创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值。

语法

fromkeys()方法语法：

dict.fromkeys(seq[, value])
参数

seq -- 字典键值列表。
value -- 可选参数, 设置键序列（seq）的值。
返回值

该方法返回列表。

实例

以下实例展示了 fromkeys()函数的使用方法：

#!/usr/bin/python 

seq =  ('name',  'age',  'sex')   

dict = dict.fromkeys(seq)  
print  "New Dictionary : %s"  % str(dict)   
dict = dict.fromkeys(seq,  10)    
print  "New Dictionary : %s"  % str(dict)
以上实例输出结果为：

New  Dictionary  :  {'age':  None,  'name':  None,  'sex':  None}   
New  Dictionary  :  {'age':  10,  'name':  10,  'sex':  10}  
