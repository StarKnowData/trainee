Python time ctime()方法
=====================

* * *

描述
--

Python time ctime() 函数把一个时间戳（按秒计算的浮点数）转化为time.asctime()的形式。 如果参数未给或者为None的时候，将会默认time.time()为参数。它的作用相当于 asctime(localtime(secs))。

语法
--

ctime()方法语法：
```
time.ctime([ sec ])
```
参数
--

*   sec -- 要转换为字符串时间的秒数。

返回值
---

该函数没有任何返回值。

实例
--

以下实例展示了 ctime() 函数的使用方法：
```
#!/usr/bin/python
import time

print "time.ctime() : %s" % time.ctime()
```
以上实例输出结果为：
```
time.ctime() : Tue Feb 17 10:00:18 2013
```