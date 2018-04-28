Python 循环嵌套
===========

 Python 语言允许在一个循环体里面嵌入另一个循环。

 **Python for 循环嵌套语法：**

  <pre>

for iterating_var in sequence:
   for iterating_var in sequence:
      statements(s)
statements(s)
</pre>

  **Python while 循环嵌套语法：**

  <pre>

while expression:
   while expression:
      statement(s)
statement(s)
</pre>

  你可以在循环体内嵌入其他的循环体，如在while循环中可以嵌入for循环， 反之，你可以在for循环中嵌入while循环。

 **实例：**

 以下实例使用了嵌套循环输出2~100之间的素数：

  实例
--

 <pre>

#!/usr/bin/python
# -*- coding: UTF-8 -*-
i = 2
while(i < 100):
   j = 2
while(j <= (i/j)):
      if not(i%j): break
j = j + 1
if (j > i/j) : print i, " 是素数"
i = i + 1
print "Good bye!"
</pre>

  以上实例输出结果: 

 
```

2 是素数
3 是素数
5 是素数
7 是素数
11 是素数
13 是素数
17 是素数
19 是素数
23 是素数
29 是素数
31 是素数
37 是素数
41 是素数
43 是素数
47 是素数
53 是素数
59 是素数
61 是素数
67 是素数
71 是素数
73 是素数
79 是素数
83 是素数
89 是素数
97 是素数
Good bye!

```

