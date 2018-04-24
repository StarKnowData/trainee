Python 练习实例98
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件"test"中保存。

**程序分析：**无。

程序源代码：

实例
--
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  if  \_\_name\_\_ == '\_\_main\_\_': fp = open('test.txt','w')  string = raw_input('please input a string:\\n')  string = string.upper()  fp.write(string)  fp = open('test.txt','r')  print  fp.read()  fp.close()
```
以上实例输出结果为：
```
please input a string:
runoob.com
RUNOOB.COM
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)```