Python 练习实例71
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**编写input()和output()函数输入，输出5个学生的数据记录。

**程序分析：**无。

程序源代码：

实例
--
```
#!/usr/bin/python  \# -*- coding: UTF-8 -*-  N = 3  #stu  \# num : string  \# name : string  \# score\[4\]: list  student = \[\]  for  i  in  range(5): student.append(\['','',\[\]\])  def  input_stu(stu): for  i  in  range(N): stu\[i\]\[0\] = raw_input('input student num:\\n')  stu\[i\]\[1\] = raw_input('input student name:\\n')  for  j  in  range(3): stu\[i\]\[2\].append(int(raw_input('score:\\n')))  def  output_stu(stu): for  i  in  range(N): print  '%-6s%-10s' % (  stu\[i\]\[0\],stu\[i\]\[1\]  )  for  j  in  range(3): print  '%-8d' % stu\[i\]\[2\]\[j\]  if  \_\_name\_\_ == '\_\_main\_\_': input_stu(student)  print  student  output_stu(student)
```
以上实例输出结果为：
```
input student num:  2 input student name: aaa
score:  89 score:  98 score:  67 input student num: bbb
input student name: ccc
score:  87 score:  45 score:  68 input student num: ddd
input student name: eee
score:  56 score:  78 score:  56  \[\['2',  'aaa',  \[89,  98,  67\]\],  \['bbb',  'ccc',  \[87,  45,  68\]\],  \['ddd',  'eee',  \[56,  78,  56\]\],  \['',  '',  \[\]\],  \['',  '',  \[\]\]\]  2 aaa 89  98  67 bbb   ccc 87  45  68 ddd   eee 56  78  56  
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)