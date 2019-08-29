#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 将时间戳改为年-月-日 时-分-秒

import time
def change(havTime):
    # 转成 localtime
    time_local = time.localtime(havTime)
    # 转成新的时间格式(如 2019-08-28 11:02:50)
    dt = time.strftime("%Y-%m-%d %H:%M:%S",time_local)
    return dt