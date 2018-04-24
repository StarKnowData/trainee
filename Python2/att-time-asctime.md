Python time asctime()方法
=======================

* * *

描述
--

Python time asctime() 函数接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。

语法
--

asctime()方法语法：
```
time.asctime(\[t\]))
```
参数
--

*   t -- 9个元素的元组或者通过函数 gmtime() 或 localtime() 返回的时间值。

返回值
---

返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。

实例
--

以下实例展示了 asctime()函数的使用方法：
```
#!/usr/bin/python
import time

t = time.localtime()
print "time.asctime(t): %s " % time.asctime(t)
```
以上实例输出结果为：
```
time.asctime(t): Tue Feb 17 09:42:58 2009
```