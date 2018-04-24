Python continue 语句
==================

Python continue 语句跳出本次循环，而break跳出整个循环。

continue 语句用来告诉Python跳过当前循环的剩余语句，然后继续进行下一轮循环。

continue语句用在while和for循环中。

**Python 语言 continue 语句语法格式如下：**

continue

**流程图：**

![cpp_continue_statement](http://www.runoob.com/wp-content/uploads/2013/11/cpp_continue_statement.jpg)

**实例：**

实例(Python 2.0+)
---------------
```
#!/usr/bin/python  
\# -*- coding: UTF-8 -*-  

for  letter  in  'Python':
\# 第一个实例 
if  letter == 'h': continue
print  '当前字母 :',
letter  var = 10
\# 第二个实例 
while  var \> 0: var = var -1 
if  var == 5: continue  
print  '当前变量值 :', var 
print  "Good bye!"
```
以上实例执行结果：
```
当前字母  : P 
当前字母  : y 
当前字母  : t 
当前字母  : o 
当前字母  : n 
当前变量值  :  9 
当前变量值  :  8 
当前变量值  :  7
当前变量值  :  6
当前变量值  :  4  
当前变量值  :  3  
当前变量值  :  2  
当前变量值  :  1  
当前变量值  :  0  
Good bye!
```