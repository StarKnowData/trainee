#!/usr/bin/env python
# coding: utf-8

# ## 题目：练习函数调用。
# 
# ## 程序分析：无。
# ### 程序：

# In[1]:


#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
def hello_world():
    print("hello world")
 
def three_hellos():
    for i in range(3):
        hello_world()
if __name__ == '__main__':
    three_hellos()


# In[ ]:




