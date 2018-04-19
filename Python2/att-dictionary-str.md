Python 字典(Dictionary) str()方法

描述

Python 字典(Dictionary) str() 函数将值转化为适于人阅读的形式，以可打印的字符串表示。

语法

str()方法语法：

str(dict)
参数

dict -- 字典。
返回值

返回字符串。

实例

以下实例展示了 str()函数的使用方法：

#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7};
print "Equivalent String : %s" % str (dict)
以上实例输出结果为：

Equivalent String : {'Age': 7, 'Name': 'Zara'}
