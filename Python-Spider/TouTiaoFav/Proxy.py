#!/usr/bin/env python
# -*- coding:utf-8 -*-

# 使用代理，防止被封 IP

import random

proxies_list = [{'HTTPS':'120.83.107.183:9999'},
                {'HTTP','27.42.168.46:8919'}]

def get():
    proxy = random.choice(proxies_list)
    return proxy