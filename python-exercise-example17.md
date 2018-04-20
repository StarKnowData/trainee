Python 练习实例17
=============

 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)

**题目：**输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

**程序分析：**利用 while 或 for 语句,条件为输入的字符不为 '\\n'。

实例 \- 使用 while 循环
-----------------
```
#!/usr/bin/python  
\# -*- coding: UTF-8 -*- 
import  string  s = raw_input('请输入一个字符串:\\n')  
letters = 0  space = 0  digit = 0 
others = 0  i=0  
while  i < len(s): c = s\[i\]  i += 1 
if  c.isalpha(): 
lette
rs += 1 
elif  
c.isspace():
space += 1 
elif  
c.isdigit(): 
digit += 1 
else: 
others += 1 
print  'char = %d,space = %d,
digit = %d,others = %d' % (letters,space,digit,others)
```
实例 \- 使用 for 循环
---------------
```
#!/usr/bin/python 

\# -*- coding: UTF-8 -*- 

import  string  s = raw_input('请输入一个字符串:\\n')  
letters = 0  space = 0  digit = 0  others = 0 
for  c  in  s: 
if  c.isalpha(): letters += 1  
elif  c.isspace(): 
space += 1  
elif  c.isdigit(): 
digit += 1  
else: 
others += 1  
print  'char = %d,space = %d,
digit = %d,others = %d' % (letters,space,digit,others)
```
以上实例输出结果为：
```
请输入一个字符串:
123runoobc  kdf235*(dfl
char = 13,space = 2,digit = 6,others = 2
```
 [![Python 100例](../images/up.gif) Python 100例](python-100-examples.html)