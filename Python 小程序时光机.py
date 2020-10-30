#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 19:35:58 2019

@author: lw
"""

import time
import datetime
import sys
print('输入指定日期即可穿越(只能到未来)'"\n"'请输入目标年月日：')
y=int(input('年'))
m=int(input('月'))
d=int(input('日'))
sj=str(y)+' '+str(m)+' '+str(d)
d1=datetime.datetime(y,m,d)
print('启动中，还需要')
while True:
   d2=datetime.datetime.now()
   sec=round((d1-d2).total_seconds())
   op=[int(sec/86400),'天',int((sec-int(sec/86400)*86400)/3600),'小时',int((sec-int(sec/3600)*3600)/60),'分',int((sec-int(sec/60)*60)),'秒']
   nn=(''.join('%s' %id for id in op))
   sys.stdout.write("\r%s"%nn)
   sys.stdout.write('即可启动')
   sys.stdout.flush()
   time.sleep(1)
