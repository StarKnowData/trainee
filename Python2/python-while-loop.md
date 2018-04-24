Python While 循环语句
=================

Python 编程中 while 语句用于循环执行程序，即在某条件下，循环执行某段程序，以处理需要重复处理的相同任务。其基本形式为：

while  判断条件：  执行语句……

执行语句可以是单个语句或语句块。判断条件可以是任何表达式，任何非零、或非空（null）的值均为true。

当判断条件假false时，循环结束。

执行流程图如下：

![python_while_loop](http://www.runoob.com/wp-content/uploads/2013/11/python_while_loop.jpg)

### Gif 演示 Python while 语句执行过程

![](http://www.runoob.com/wp-content/uploads/2013/11/loop-over-python-list-animation.gif)

实例
--
```
#!/usr/bin/python  count = 0  while  (count < 9): print  'The count is:', count  count = count \+ 1  print  "Good bye!"

 ``` 
[运行实例 »](http://www.runoob.com/try/runcode.php?filename=test_while&type=python)

以上代码执行输出结果:
```
The count is:  0  The count is:  1  The count is:  2  The count is:  3  The count is:  4  The count is:  5  The count is:  6  The count is:  7  The count is:  8  Good bye!
```
while 语句时还有另外两个重要的命令 continue，break 来跳过循环，continue 用于跳过该次循环，break 则是用于退出循环，此外"判断条件"还可以是个常值，表示循环必定成立，具体用法如下：
```
\# continue 和 break 用法  i = 1  while  i < 10: i += 1  if  i%2 \> 0: \# 非双数时跳过输出  continue  print  i  \# 输出双数2、4、6、8、10  i = 1  while  1: \# 循环条件为1必定成立  print  i  \# 输出1~10  i += 1  if  i \> 10: \# 当i大于10时跳出循环  break
```
  

* * *

无限循环
----

如果条件判断语句永远为 true，循环将会无限的执行下去，如下实例：

实例
--
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  var = 1  while  var == 1 : \# 该条件永远为true，循环将无限执行下去  num = raw_input("Enter a number :")  print  "You entered: ", num  print  "Good bye!"
```
以上实例输出结果：
```
Enter a number :20  You entered:  20  Enter a number :29  You entered:  29  Enter a number :3  You entered:  3  Enter a number between :Traceback  (most recent call last):  File  "test.py", line 5,  in  <module> num = raw_input("Enter a number :")  KeyboardInterrupt
```
**注意：**以上的无限循环你可以使用 CTRL+C 来中断循环。

  

* * *

循环使用 else 语句
------------

在 python 中，while … else 在循环条件为 false 时执行 else 语句块：

实例
--
```
#!/usr/bin/python  count = 0  while  count < 5: print  count, " is less than 5"  count = count \+ 1  else: print  count, " is not less than 5"
```
以上实例输出结果为：
```
0  is less than 5  1  is less than 5  2  is less than 5  3  is less than 5  4  is less than 5  5  is  not less than 5

  ```

* * *

简单语句组
-----

类似 if 语句的语法，如果你的 while 循环体中只有一条语句，你可以将该语句与while写在同一行中， 如下所示：

实例
--

#!/usr/bin/python  flag = 1  while  (flag): print  'Given flag is really true!'  print  "Good bye!"

**注意：**以上的无限循环你可以使用 CTRL+C 来中断循环。