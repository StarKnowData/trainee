#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time

import math

import hashlib

def getASCP():
    """
    获取 AS CP 参数
    :return:
    """
    t = int(math.floor(time.time()))
    e = hex(t).upper()[2:]
    m = hashlib.md5()
    m.update(str(t).encode(encoding='utf-8'))
    i = m.hexdigest().upper()

    if len(e) != 8:
        AS = '479BB4B7254C150'
        CP = '7E0AC8874BB0985'
        return AS,CP
    n = i[0:5]
    a = i[-5:]
    s = ''
    r = ''
    for o in range(5):
        s += n[o] + e[o]
        r += e[o+3] + a[o]

    AS = 'A1'+ s + e[-3:]
    CP = e[o+3] + a[o]

    return AS,CP

def get():
    """
    获取 AS CP 时间戳，并存入其中
    :return:
    """

    ASCP = ()
    ASCP = getASCP()
    return (ASCP[0],ASCP[1],int(time.time()))
