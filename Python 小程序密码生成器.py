#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 19:34:39 2019

@author: lw
"""

x=int(input())
print(''.join(__import__('random')
.choice('QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm!@#$%^&*()_+=}{[]:;<,.>?/1234567890') 
        for i in range(x)))
