Python 练习实例46
=============


**题目：** 求输入数字的平方，如果平方运算后小于 50 则退出。

**程序分析：** 无

程序源代码：

实例(Python 2.0+)
---------------

```python

#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
TRUE = 1
FALSE = 0
def SQ(x):
    return x * x
print '如果输入的数字小于 50，程序将停止运行。'
again = 1
while again:
    num = int(raw_input('请输入一个数字：'))
    print '运算结果为: %d' % (SQ(num))
    if SQ(num) >= 50:
        again = TRUE
    else:
        again = FALSE

```

以上实例输出结果为：

```
如果输入的数字小于 50，程序将停止运行。
请输入一个数字：12
运算结果为: 144
请输入一个数字：14
运算结果为: 196
请输入一个数字：1
运算结果为: 1
```


