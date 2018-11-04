#coding=utf8
# python3.6.5
# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests
from ShowapiRequest import ShowapiRequest

r = ShowapiRequest("http://route.showapi.com/60-27","71575","f49b33e5f33946e1aab16e4a831800a7" )
r.addBodyPara("info", "王健林")
r.addBodyPara("userid", "userid")
# r.addFilePara("img", r"C:\Users\showa\Desktop\使用过的\4.png") #文件上传时设置
res = r.post()
print(res.text) # 返回信息