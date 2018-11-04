#!/usr/bin/env python
# coding: utf-8

# # Python 练习实例82

# ## 题目：八进制转换为十进制

# In[4]:


#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
if __name__ == '__main__':
    n = 0
    p = input('input a octal number:\n')
    for i in range(len(p)):
        n = n * 8 + ord(p[i]) - ord('0')
    print (n)

