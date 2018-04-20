Python time clock()方法
=====================

* * *

描述
--

Python time clock() 函数以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。

这个需要注意，在不同的系统上含义不同。在UNIX系统上，它返回的是"进程时间"，它是用秒表示的浮点数（时间戳）。而在WINDOWS中，第一次调用，返回的是进程运行的实际时间。而第二次之后的调用是自第一次调用以后到现在的运行时间。（实际上是以WIN32上QueryPerformanceCounter()为基础，它比毫秒表示更为精确）

语法
--

clock()方法语法：
```
time.clock()
```
参数
--

*   NA。

返回值
---

该函数有两个功能，

在第一次调用的时候，返回的是程序运行的实际时间；

以第二次之后的调用，返回的是自第一次调用后,到这次调用的时间间隔

在win32系统下，这个函数返回的是真实时间（wall time），而在Unix/Linux下返回的是CPU时间。

实例
--

以下实例展示了 clock()函数的使用方法：
```
#!/usr/bin/python  

import time def procedure():  
time.sleep(2.5)    \# measure process time t0 = time.clock() procedure()   
print time.clock()  - t0,  "seconds process time"  \# measure wall time t0 = time.time() procedure()   
print time.time()  - t0,  "seconds wall time"
```
以上实例输出结果为：
```
0.0 seconds process time 2.50023603439 seconds wall time
```