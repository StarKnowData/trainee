Python time time()方法
====================

* * *

描述
--

Python time time() 返回当前时间的时间戳（1970纪元后经过的浮点秒数）。

语法
--

time()方法语法：
```
time.time()
```
参数
--

*   NA。

返回值
---

返回当前时间的时间戳（1970纪元后经过的浮点秒数）。

实例
--

以下实例展示了 time() 函数的使用方法：
```
#!/usr/bin/python
import time

print "time.time(): %f " %  time.time()
print time.localtime( time.time() )
print time.asctime( time.localtime(time.time()) )
```
以上实例输出结果为：
```
time.time(): 1234892919.655932
(2009, 2, 17, 10, 48, 39, 1, 48, 0)
Tue Feb 17 10:48:39 2009
```