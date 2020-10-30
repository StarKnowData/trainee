#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 19:38:58 2019

@author: lw
"""

__author__ = "Gavin"
import random
checkcode=''
for i in range(5):
    current = random.randrange(0,5)
    if current == i:
        tmp=chr(random.randint(65,90))
    else:
        tmp=random.randint(0,9)
    checkcode += str(tmp)
    
print(checkcode)