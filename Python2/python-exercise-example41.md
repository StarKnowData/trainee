Python 练习实例41
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**模仿静态变量的用法。

**程序分析：**无。

程序源代码：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

def varfunc():
    var = 0
    print 'var = %d' % var
    var += 1
if \_\_name\_\_ == '\_\_main\_\_':
    for i in range(3):
        varfunc()

\# 类的属性
\# 作为类的一个属性吧
class Static:
    StaticVar = 5
    def varfunc(self):
        self.StaticVar += 1
        print self.StaticVar

print Static.StaticVar
a = Static()
for i in range(3):
    a.varfunc()
```
以上实例输出结果为：
```
var = 0
var = 0
var = 0
5
6
7
8
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)