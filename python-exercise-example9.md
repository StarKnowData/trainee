Python 练习实例9
============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**暂停一秒输出。

**程序分析：**使用 time 模块的 sleep() 函数。

程序源代码：

实例
--
```
#!/usr/bin/python  
\# -*- coding: UTF-8 -*- 
import  time  myD = {1: 'a', 2: 'b'}
for  key, value  in  dict.items(myD): 
print  key, value  time.sleep(1)  
\# 暂停 1 秒
```
以上实例输出结果为(会有停顿效果)：
```
1 a
2 b
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)