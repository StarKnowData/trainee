Python time altzone()方法
=======================

* * *

描述
--

Python time altzone() 函数返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。

语法
--

altzone()方法语法：
```
time.altzone
```
参数
--

*   NA。

返回值
---

返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。

实例
--

以下实例展示了 altzone()函数的使用方法：
```
#!/usr/bin/python 

import time  
print  "time.altzone %d "  % time.altzone
```
以上实例输出结果为：
```
time.altzone()  25200
```