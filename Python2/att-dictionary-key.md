Python 字典(Dictionary) has_key()方法
=================================

* * *

描述
--

Python 字典(Dictionary) has_key() 函数用于判断键是否存在于字典中，如果键在字典dict里返回true，否则返回false。

语法
--

has_key()方法语法：

dict.has_key(key)

参数
--

*   key -- 要在字典中查找的键。

返回值
---

如果键在字典里返回true，否则返回false。

实例
--

以下实例展示了 has_key()函数的使用方法：

#!/usr/bin/python dict =  {'Name':  'Zara',  'Age':  7}  print  "Value : %s"  % dict.has_key('Age')  print  "Value : %s"  % dict.has_key('Sex')

以上实例输出结果为：

Value  :  True  Value  :  False
