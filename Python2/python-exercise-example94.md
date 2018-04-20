Python 练习实例94
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**时间函数举例4,一个猜数游戏，判断一个人反应快慢。

**程序分析：**无。

程序源代码：
```
实例(Python 2.0+)
---------------

#!/usr/bin/python  \# -*- coding: UTF-8 -*-  if  \_\_name\_\_ == '\_\_main\_\_': import  time  import  random  play_it = raw_input('do you want to play it.(\\'y\\' or \\'n\\')')  while  play_it == 'y': c = raw_input('input a character:\\n')  i = random.randint(0,2**32) % 100  print  'please input number you guess:\\n'  start = time.clock()  a = time.time()  guess = int(raw_input('input your guess:\\n'))  while  guess != i: if  guess \> i: print  'please input a little smaller'  guess = int(raw_input('input your guess:\\n'))  else: print  'please input a little bigger'  guess = int(raw_input('input your guess:\\n'))  end = time.clock()  b = time.time()  var = (end \- start) / 18.2  print  var  \# print 'It took you %6.3 seconds' % time.difftime(b,a))  if  var < 15: print  'you are very clever!'  elif  var < 25: print  'you are normal!'  else: print  'you are stupid!'  print  'Congradulations'  print  'The number you guess is %d' % i  play_it = raw_input('do you want to play it.')
```
以上实例输出结果为：
```
do you want to play it.('y' or 'n')y
input a character:
5
please input number you guess:

input your guess:
60
……
please input a little bigger
input your guess:
29
please input a little smaller
input your guess:
28
3.81868131868e-05
you are very clever!
Congradulations
The number you guess is 28
do you want to play it.
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)