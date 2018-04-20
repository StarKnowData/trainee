Python break 语句
===============

Python break语句，就像在C语言中，打破了最小封闭for或while循环。

break语句用来终止循环语句，即循环条件没有False条件或者序列还没被完全递归完，也会停止执行循环语句。

break语句用在while和for循环中。

如果您使用嵌套循环，break语句将停止执行最深层的循环，并开始执行下一行代码。

**Python语言 break 语句语法：**

break

**流程图：**

![](http://www.runoob.com/wp-content/uploads/2013/11/cpp_break_statement.jpg)

实例(Python 2.0+)
---------------
```
#!/usr/bin/python    
\# -*- coding: UTF-8 -*-   
for  letter  in  'Python': 
\# 第一个实例  
if  letter == 'h': break   
print  '当前字母 :', letter  var = 10    
\# 第二个实例  while  var \> 0:  
print  '当前变量值 :', var  var = var -1    
if  var == 5: \# 当变量 var 等于 5 时退出循环  
break  print  "Good bye!"
```
以上实例执行结果：
```
当前字母 : P
当前字母 : y
当前字母 : t
当前变量值 : 10
当前变量值 : 9
当前变量值 : 8
当前变量值 : 7
当前变量值 : 6
Good bye!
```