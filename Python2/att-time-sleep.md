Python time sleep()方法
=====================

* * *

描述
--

Python time sleep() 函数推迟调用线程的运行，可通过参数secs指秒数，表示进程挂起的时间。

语法
--

sleep()方法语法：
```
time.sleep(t)
```
参数
--

*   t -- 推迟执行的秒数。

返回值
---

该函数没有返回值。

实例
--

以下实例展示了 sleep() 函数的使用方法：

实例
--
```
#!/usr/bin/python 

import  time    
print  "Start : %s" % time.ctime()  time.sleep(  5  )    
print  "End : %s" % time.ctime()
```
以上实例输出结果为：
```
Start  :  Tue  Feb  17  10:19:18  2013  End  :  Tue  Feb  17  10:19:23  
```