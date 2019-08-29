#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import ASCP
import Proxy
import time
import TimeChange
import xlwt
import datetime




# 打开表格，初始化

workBook = xlwt.Workbook

ws = workBook.add_sheet(sheetname='sheet1', cell_overwrite_ok=True)

row0 = [u'分类',u'标题',u'发布时间',u'作者',u'原地址']

style0 = xlwt.easyxf('font: name Times New Roman, color-index red, bold on',num_format_str='#,##0.00') # 设置单元格字体和颜色

for g in range(0,len(row0)):
    ws.write(0,g,row0[g],style0)


newAddress = '0' # 指向下一个 URL 地址的关键值,初始值为 0，在每页列表的最后一栏获取

for pageNum in range(0,33):
    AS = ASCP.get()[0] # 获取 as
    CP = ASCP.get()[1] # 获取 cp
    Time = ASCP.get()[2] # 获取当前时间戳
    import requests

    url = "https://www.toutiao.com/c/user/favourite/"

    querystring = {"page_type": "2", "user_id": "3130526840", "max_behot_time": "0", "count": "20",
                   "as": AS, "cp": CP, "_signature": "jaoxRhAT0Nxj7G4N0jeM6I2qMV",
                   "max_repin_time": "0"}

    headers = {
        'sec-fetch-mode': "cors",
        'dnt': "1",
        'accept-encoding': "gzip, deflate, br",
        'accept-language': "zh-CN,zh;q=0.9,en;q=0.8,id;q=0.7,ru;q=0.6,fil;q=0.5,ja;q=0.4,vi;q=0.3",
        'x-requested-with': "XMLHttpRequest",
        'cookie': "tt_webid=6729316863161419271; WEATHER_CITY=%E5%8C%97%E4%BA%AC; tt_webid=6729316863161419271; csrftoken=027825dfd00b005c403bf853420d543a; sso_uid_tt=e3886281f0ab0d027be4f761ccd6f1a4; toutiao_sso_user=f3ce1adcfd0875ed4a1fc063007a4155; login_flag=a2338aefe392b5ae622d5c21f9b1566e; sessionid=2e60c4d053850d7642c057d2169b60c2; uid_tt=4c38516716d6a0b19d4271518097d326; sid_tt=2e60c4d053850d7642c057d2169b60c2; sid_guard='2e60c4d053850d7642c057d2169b60c2 | 1566791197 | 15552000 | Sat\054 22 - Feb - 2020 03: 46:37 GMT'; uuid='w: cc98fc5c0c464ad999663bf78f3cfbc4'; __tasessionId=i88fqog151566962264026",
        'pragma': "no-cache",
        'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
        'content-type': "application/x-www-form-urlencoded",
        'accept': "application/json, text/javascript",
        'cache-control': "no-cache,no-cache",
        'authority': "www.toutiao.com",
        'referer': "https://www.toutiao.com/c/user/3130526840/",
        'sec-fetch-site': "same-origin",
        'Postman-Token': "5c767c90-569a-4e3a-9f75-5e94aaa6c599,876c5e5c-1868-432a-80cc-3360b1c5f5ff",
        'Host': "www.toutiao.com",
        'Connection': "keep-alive"
    }

    # response = requests.request("GET", url, headers=headers, params=querystring)
    response = requests.request("GET", url, headers=headers, params=querystring)

    response.encoding = 'utf-8'
    # print(response.text)
    newsData = response.json()['data'] # 获取每页收藏列表

    try:
        newAddress = str(newsData[len(newsData)-1]['repin_time'])
    except IndexError:
        pass

    for countNum in range(0,len(newsData)):
        try:
            havTitle = newsData[countNum]['title'] # title
            havTag   = newsData[countNum]['chinese_tag'] # 分类
            havSource = newsData[countNum]['source'] # 分类
            havAddress = newsData[countNum]['display_url'] # 源地址
            havTime  = newsData[countNum]['behot_time'] # 发布时间

        except IndexError:
            pass

        for g in range(0,len(row0)):
            ws.write(pageNum*20+countNum+1,0,havTag)
            ws.write(pageNum*20+countNum+1,1,havTitle)
            ws.write(pageNum*20+countNum+1,2,TimeChange.change(havTime))
            ws.write(pageNum*20+countNum+1,3,havSource)
            ws.write(pageNum*20+countNum+1,4,havAddress)

    time.sleep(3)


workBook.save('头条%s.xls' % str(datetime.date.today()))