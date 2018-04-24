Python 练习实例35
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**文本颜色设置。

**程序分析：**无。

实例
--
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  class  bcolors: HEADER = '\\033\[95m'  OKBLUE = '\\033\[94m'  OKGREEN = '\\033\[92m'  WARNING = '\\033\[93m'  FAIL = '\\033\[91m'  ENDC = '\\033\[0m'  BOLD = '\\033\[1m'  UNDERLINE = '\\033\[4m'  print  bcolors.WARNING \+ "警告的颜色字体?" \+ bcolors.ENDC
```
以上实例输出结果为：
```
警告的颜色字体?    # 浅黄色
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)