#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 12 19:14:17 2019

@author: lw
"""

#这是一个猜数字游戏。1-100之间数字猜测
import random
num=random.randint(1,100)
print('这是一个猜数字游戏，你可以输入1到100之间的数字，但是只有5次机会')

for guesstake in range(1,6):
    print('请输入一个数字')
    guess=int(input())

    if guess < num:
        print('你输入的数字太小了')
    elif guess > num:
        print('你输入的数字太大了')
    else:
        break

if guess == num:
    print('恭喜！你猜对了!你用了'+ str(guesstake) +'次')
else:
    print('数字是'+ str(num) +' 继续努力！')
input()
