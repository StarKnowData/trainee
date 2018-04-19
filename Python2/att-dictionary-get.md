Python 字典(Dictionary) get()方法

描述

Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。

语法

get()方法语法：

dict.get(key,  default=None)
参数

key -- 字典中要查找的键。
default -- 如果指定键的值不存在时，返回该默认值值。
返回值

返回指定键的值，如果值不在字典中返回默认值None。

实例

以下实例展示了 get()函数的使用方法：

#!/usr/bin/python 

dict =  {'Name':  'Zara',  'Age':  27}   

print  "Value : %s"  % dict.get('Age')  
print  "Value : %s"  % dict.get('Sex',  "Never")  
以上实例输出结果为：

Value  :  27  
Value  :  Never  
