Python 字典(Dictionary) type()方法

描述

Python 字典(Dictionary) type() 函数返回输入的变量类型，如果变量是字典就返回字典类型。

语法

type()方法语法：

type(dict)
参数

dict -- 字典。
返回值

返回输入的变量类型。

实例

以下实例展示了 type()函数的使用方法：

#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7};

print "Variable Type : %s" %  type (dict)
以上实例输出结果为：

Variable Type : <type 'dict'>
