Python time localtime()方法
=========================

* * *

描述
--

Python time localtime() 函数类似gmtime()，作用是格式化时间戳为本地的时间。 如果sec参数未输入，则以当前时间为转换标准。 DST (Daylight Savings Time) flag (-1, 0 or 1) 是否是夏令时。

语法
--

localtime()方法语法：
```
time.localtime([ sec ])
```
参数
--

*   sec -- 转换为time.struct_time类型的对象的秒数。

返回值
---

该函数没有任何返回值。

实例
--

以下实例展示了 localtime() 函数的使用方法：

实例
--
```
#!/usr/bin/python  

import  time   
print  "time.localtime() : %s" % time.localtime()
```
以上实例输出结果为：
```
time.localtime() : time.struct_time(tm_year=2016, tm_mon=11, tm_mday=27, tm_hour=10, tm_min=26, tm_sec=5, tm_wday=6, tm_yday=332, tm_isdst=0)
```