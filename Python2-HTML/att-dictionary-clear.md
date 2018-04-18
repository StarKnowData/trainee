Python 字典(Dictionary) clear()方法

描述

Python 字典(Dictionary) clear() 函数用于删除字典内所有元素。

语法

clear()方法语法：

dict.clear()
参数

NA。
返回值

该函数没有任何返回值。

实例

以下实例展示了 clear()函数的使用方法：

#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7};

print "Start Len : %d" %  len(dict)
dict.clear()
print "End Len : %d" %  len(dict)
以上实例输出结果为：

Start Len : 2
End Len : 0
