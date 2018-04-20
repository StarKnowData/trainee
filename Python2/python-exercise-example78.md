Python 练习实例78
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**找到年龄最大的人，并输出。请找出程序中有什么问题。

**程序分析：**无。

程序源代码：
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  if  \_\_name\_\_ == '\_\_main\_\_': person = {"li":18,"wang":50,"zhang":20,"sun":22} m = 'li'  for  key  in  person.keys(): if  person\[m\] < person\[key\]: m = key  print  '%s,%d' % (m,person\[m\])
```
以上实例输出结果为：
```
wang,50
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)