# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 09:07:26 2018

@author: aike
"""

import pandas as pd
import numpy as np
from numpy.random import rand as rd
from numpy.random import random_integers as ri
import random  
rrr={'weather':['cold','hot','cold','hot','cold','hot','cold'],'Food':['soup','soup','soup','icecream','icecream','icecream','chocolate'],'price':10*rd(7),'Number':[1,2,6,4,7,8,9]}
df=pd.DataFrame(rrr)
weather_group=df.groupby('weather')
print(weather_group.agg([np.mean,np.median]))
i=0
for name,group  in weather_group:
    i=i+1;
    print('group',i,name)
    print(group)    
wg=df.groupby(['weather','Food'])
print(wg.groups)

ed=pd.DataFrame({'empnr':[5,3,9],'dest':['hague','amsterdam','rotterdam']})
ea=pd.DataFrame({'empnr':[5,9,7],'amount':[10,5,2.5]})
em1=pd.merge(ed,ea,on='empnr')
em2=pd.merge(ed,ea,how='inner')
em3=pd.merge(ed,ea,how='outer')
em4=pd.merge(ed,ea,left_on='dest',right_on='amount',how='outer')
em5=pd.merge(ed,ea,left_on='empnr',right_on='empnr',how='outer')
em6=pd.merge(ed,ea,left_on='dest',right_on='amount',how='outer')
help(pd.merge)