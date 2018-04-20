Python time gmtime()方法
======================

* * *

描述
--

Python time gmtime() 函数将一个时间戳转换为UTC时区（0时区）的struct\_time，可选的参数sec表示从1970-1-1以来的秒数。其默认值为time.time()，函数返回time.struct\_time类型的对象。（struct_time是在time模块中定义的表示时间的对象）。

语法
--

gmtime()方法语法：
```
time.gmtime([ sec ])
```
参数
--

*   sec -- 转换为time.struct_time类型的对象的秒数。

返回值
---

该函数没有任何返回值。

实例
--

以下实例展示了 gmtime() 函数的使用方法：
```
#!/usr/bin/python   

import time  
print  "time.gmtime() :  %s"  % time.gmtime()
```
以上实例输出结果为：
```
time.gmtime()  :  time.struct_time(tm_year=2016,tm_mon=4, tm_mday=7, tm_hour=2, tm_min=55, tm_sec=45, tm_wday=3, tm_yday=98, tm_isdst=0)
```