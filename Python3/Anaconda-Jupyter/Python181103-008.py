#!/usr/bin/env python
# coding: utf-8

# 题目：输出 9*9 乘法口诀表。
# 
# 程序分析：分行与列考虑，共9行9列，i控制行，j控制列。
# 
# 程序源代码：

# In[3]:


#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
for i in range(1, 10):
    print 
    for j in range(1, i+1):
        print (i, j, i*j),


# In[ ]:




