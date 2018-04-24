Python 练习实例43
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**模仿静态变量(static)另一案例。

**程序分析：**演示一个python作用域使用方法

程序源代码：
```
#!/usr/bin/python
\# -*- coding: UTF-8 -*-

class Num:
    nNum = 1
    def inc(self):
        self.nNum += 1
        print 'nNum = %d' % self.nNum

if \_\_name\_\_ == '\_\_main\_\_':
    nNum = 2
    inst = Num()
    for i in range(3):
        nNum += 1
        print 'The num = %d' % nNum
        inst.inc()
```
以上实例输出结果为：
```
The num = 3
nNum = 2
The num = 4
nNum = 3
The num = 5
nNum = 4
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)