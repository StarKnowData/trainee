# coding=utf-8

## 需要 Python2.7

## 在 MySQL 教程中通过正则表达式,^!\[\d+]\(.*\) 查到得到所有的连接的列表

## 替换得到所有的连接

## 使用 ^!\[\d+]\( 替换

##

## 保存结束后:

## ![1](http://img.blog.csdn.net/20170505141901715) 替换为

## ![1](./images/20170505141901715)

## 替换 \(\.\/images\/\d+

## 为 $0.png


# import 是在导入
# requests 是网络请求的包
# request 的常用方法有.



import requests
import urllib2
import os

content = [
'http://img.blog.csdn.net/20170505141901715',
'http://img.blog.csdn.net/20170505145310466',
'http://img.blog.csdn.net/20170505142119893',
'http://img.blog.csdn.net/20170505143557398',
'http://img.blog.csdn.net/20170505184606504',
'http://img.blog.csdn.net/20170505185330045',
'http://img.blog.csdn.net/20170505190118166',
'http://img.blog.csdn.net/20170505190700955',
'http://img.blog.csdn.net/20170505201016682',
'http://img.blog.csdn.net/20170505214100825',
'http://img.blog.csdn.net/20170505214735859',
'http://img.blog.csdn.net/20170505215530129',
'http://img.blog.csdn.net/20170505215905568',
'http://img.blog.csdn.net/20170505220452057',
'http://img.blog.csdn.net/20170505221652339',
'http://img.blog.csdn.net/20170505222047969',
'http://img.blog.csdn.net/20170506102816519',
'http://img.blog.csdn.net/20170506105942273',
'http://img.blog.csdn.net/20170506132014635',
'http://img.blog.csdn.net/20170506132904083',
'http://img.blog.csdn.net/20170521214843424',
'http://img.blog.csdn.net/20170521215211842',
'http://img.blog.csdn.net/20170521220113393',
'http://img.blog.csdn.net/20170521223557192',
'http://img.blog.csdn.net/20170521223912147',
'http://img.blog.csdn.net/20170521224106226',
'http://img.blog.csdn.net/20170521230456356',
'http://img.blog.csdn.net/20170522161909823',
'http://img.blog.csdn.net/20170522162320934',
'http://img.blog.csdn.net/20170522163928644',
'http://img.blog.csdn.net/20170522165051589',
'http://img.blog.csdn.net/20170522165703155',
'http://img.blog.csdn.net/20170523102924169',
'http://img.blog.csdn.net/20170523120146063',
'http://img.blog.csdn.net/20170523120331562',
'http://img.blog.csdn.net/20170523121027497',
'http://img.blog.csdn.net/20170523210307014',
'http://img.blog.csdn.net/20170523211344326',
'http://img.blog.csdn.net/20170523211827926',
'http://img.blog.csdn.net/20170523212240672',
'http://img.blog.csdn.net/20170523213342164',
'http://img.blog.csdn.net/20170523214019191',
'http://img.blog.csdn.net/20170523225451048',
'http://img.blog.csdn.net/20170523230214445',
'http://img.blog.csdn.net/20170523230908501',
'http://img.blog.csdn.net/20170523233034847',
'http://img.blog.csdn.net/20170523233250704',
'http://img.blog.csdn.net/20170523234155133',
'http://img.blog.csdn.net/20170523234752168',
'http://img.blog.csdn.net/20170523235047044',
'http://img.blog.csdn.net/20170524000518389',
'http://img.blog.csdn.net/20170524000826628',
'http://img.blog.csdn.net/20170524090620434',
'http://img.blog.csdn.net/20170524091144437',
'http://img.blog.csdn.net/20170524091651347',
'http://img.blog.csdn.net/20170524092040004',
'http://img.blog.csdn.net/20170524092306849',
'http://img.blog.csdn.net/20170524093013603',
'http://img.blog.csdn.net/20170524093806457',
'http://img.blog.csdn.net/20170601085452637',
'http://img.blog.csdn.net/20170601085511060',
'http://img.blog.csdn.net/20170601085527435',
'http://img.blog.csdn.net/20170601085541820',
'http://img.blog.csdn.net/20170601085555233',
'http://img.blog.csdn.net/20170601085610524',
'http://img.blog.csdn.net/20170601085624014',
'http://img.blog.csdn.net/20170601085636952',
'http://img.blog.csdn.net/20170603202002804',
'http://img.blog.csdn.net/20170603202439264',
'http://img.blog.csdn.net/20170603202810534',
'http://img.blog.csdn.net/20170603203053592',
'http://img.blog.csdn.net/20170603203402011',
'http://img.blog.csdn.net/20170603205833948',
'http://img.blog.csdn.net/20170603210620720',
'http://img.blog.csdn.net/20170603210950502',
'http://img.blog.csdn.net/20170625180810447',
'http://img.blog.csdn.net/20170625180922214',
'http://img.blog.csdn.net/20170625181516023',
'http://img.blog.csdn.net/20170625182444031',
'http://img.blog.csdn.net/20170625183121678',
'http://img.blog.csdn.net/20170625210624498',
'http://img.blog.csdn.net/20170625215451466',
'http://img.blog.csdn.net/20170625220806193',
'http://img.blog.csdn.net/20170625221005836',
'http://img.blog.csdn.net/20170625221630276',
'http://img.blog.csdn.net/20170627210129189',
'http://img.blog.csdn.net/20170627210410567',
'http://img.blog.csdn.net/20170627210829379',
'http://img.blog.csdn.net/20170627211555446',
'http://img.blog.csdn.net/20170627212554643',
'http://img.blog.csdn.net/20170627213601017',
'http://img.blog.csdn.net/20170627214720585',
'http://img.blog.csdn.net/20170627215231647',
'http://img.blog.csdn.net/20170627220823491',
'http://img.blog.csdn.net/20170711085904967',
'http://img.blog.csdn.net/20170711090554273',
'http://img.blog.csdn.net/20170711091902136',
'http://img.blog.csdn.net/20170711093201665',
'http://img.blog.csdn.net/20170711192158394',
'http://img.blog.csdn.net/20170711192515751',
'http://img.blog.csdn.net/20170711212738238',
'http://img.blog.csdn.net/20170903173835484',
'http://img.blog.csdn.net/20170903174232775',
'http://img.blog.csdn.net/20170903175912316',
'http://img.blog.csdn.net/20170903180237267',
'http://img.blog.csdn.net/20170903181329186',
'http://img.blog.csdn.net/20170903182832314',
'http://img.blog.csdn.net/20170903185516278',
'http://img.blog.csdn.net/20170909134753471',
'http://img.blog.csdn.net/20170909141917265',
'http://img.blog.csdn.net/20170909143447416',
'http://img.blog.csdn.net/20170909145056989',
'http://img.blog.csdn.net/20170909150303075',
'http://img.blog.csdn.net/20170909151612737',
'http://img.blog.csdn.net/20170909152042006',
'http://img.blog.csdn.net/20170909163651397',
'http://img.blog.csdn.net/20171001124211791',
'http://img.blog.csdn.net/20171001125044817',
'http://img.blog.csdn.net/20171001125843845',
'http://img.blog.csdn.net/20171001125723307',
'http://img.blog.csdn.net/20171001130529481',
'http://img.blog.csdn.net/20171001130643315',
'http://img.blog.csdn.net/20171001185200857',
'http://img.blog.csdn.net/20171001185637160',
'http://img.blog.csdn.net/20171001190506222',
'http://img.blog.csdn.net/20171001192031438',
'http://img.blog.csdn.net/20171001193445728',
'http://img.blog.csdn.net/20171002111841764',
'http://img.blog.csdn.net/20171002112024147',
'http://img.blog.csdn.net/20171002112300870',
'http://img.blog.csdn.net/20171002113939685',
'http://img.blog.csdn.net/20171002114030390',
'http://img.blog.csdn.net/20171002114807283',
'http://img.blog.csdn.net/20171002115002641',
'http://img.blog.csdn.net/20171021195300581',
'http://img.blog.csdn.net/20171021200426871',
'http://img.blog.csdn.net/20171021201044152',
'http://img.blog.csdn.net/20171021201540765',
'http://img.blog.csdn.net/20171021202331094',
'http://img.blog.csdn.net/20171021203403955',
'http://img.blog.csdn.net/20180103220140999',
'http://img.blog.csdn.net/20180103220216878',
'http://img.blog.csdn.net/20180103220401645',
'http://img.blog.csdn.net/2018030312401492',
'http://img.blog.csdn.net/20180303124316330',
'http://img.blog.csdn.net/2018030312461235',
'http://img.blog.csdn.net/20180303125417272',
'http://img.blog.csdn.net/2018030312594361',
'http://img.blog.csdn.net/2018030313100113',
'http://img.blog.csdn.net/20180303131400954',
'http://img.blog.csdn.net/20180303134415202',
'http://img.blog.csdn.net/20180303135209908',
'http://img.blog.csdn.net/2018030313543411',
'http://img.blog.csdn.net/20180303135927583',
'http://img.blog.csdn.net/20180303142308376',
'http://img.blog.csdn.net/20180303142619986',
'http://img.blog.csdn.net/20180303145957621',
'http://img.blog.csdn.net/20180303150125572',
'http://img.blog.csdn.net/20180303152317511',
'http://img.blog.csdn.net/20180303152637538',
'http://img.blog.csdn.net/20180303152744196',
'http://img.blog.csdn.net/20180303153024878',
'http://img.blog.csdn.net/20180303153409873',
'http://img.blog.csdn.net/20180303165150957',
'http://img.blog.csdn.net/20180303165813193',
'http://img.blog.csdn.net/20180303171216448',
'http://img.blog.csdn.net/20180303171506912'
]

for imgurl in content:
    name = imgurl[-16:];
    os.chdir(r"/Users/lw/Desktop/images/")
    header = {
        'accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,id;q=0.7,ru;q=0.6,fil;q=0.5,ja;q=0.4,vi;q=0.3',
        'cache-control': 'no-cache',
        'cookie': 'uuid_tt_dd=10_19464055090-1523602035985-213426; kd_user_id=b40621ef-e62e-4aee-8683-ef57a9ad4e4e; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac = 1788 * 1 * PC_VC;smidV2 = 201806170900251e5e1c709196caec245c56cc0aee69e0009c8991fbedb8370;UN=weixin_41508953; BT=1531202493850; UM_distinctid=16482c9d70b8d1-0690b11d28f1ef-16386952-1fa400-16482c9d70cd3; dc_session_id = 10_1533124620246.234261;Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac = 1533093309, 1533101657, 1533124621, 1533124683;dc_tos = pcs6pz;Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1533124871',
        'dnt':'1',
        'pragma':'no-cache',
        'referer':'https://blog.csdn.net/qq_35246620/article/details/77606809',
        'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36'
    }
    request = urllib2.Request(imgurl, None, header)  #刻意增加头部header，否则本行与下一行可以写为：response = urllib2.urlopen(imgurl)
    response = urllib2.urlopen(request)
    f = open(name+'.png' , 'wb')
    f.write(response.read())
    f.close()
    print(imgurl)
