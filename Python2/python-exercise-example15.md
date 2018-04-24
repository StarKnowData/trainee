Python 练习实例15
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。

**程序分析：**程序分析：(a>b)?a:b这是条件运算符的基本例子。

程序源代码：

实例
--
```
#!/usr/bin/python  
\# -*- coding: UTF-8 -*- 
score = int(raw_input('输入分数:\\n'))  
if  score >= 90: grade = 'A'
elif  score >= 60: 
grade = 'B'  
else: grade = 'C'  
print  '%d 属于 %s' % (score,grade)
```
  

以上实例输出结果为：
```
输入分数:
89
89 属于 B
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)