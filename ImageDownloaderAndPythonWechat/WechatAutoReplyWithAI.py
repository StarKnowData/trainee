#coding=utf8
import itchat
import time
import json
# 自动回复
# 封装好的装饰器，当接收到的消息是Text，即文字消息
@itchat.msg_register('Text')
def text_reply(msg):
    # 当消息不是由自己发出的时候
    if not msg['FromUserName'] == myUserName:

        question = (msg['Text'])
        from ShowapiRequest import ShowapiRequest

        r = ShowapiRequest("http://route.showapi.com/60-27", "71575", "f49b33e5f33946e1aab16e4a831800a7")
        r.addBodyPara("info", question)
        r.addBodyPara("userid", "userid")
        # r.addFilePara("img", r"C:\Users\showa\Desktop\使用过的\4.png") #文件上传时设置
        res = r.post()

        dict = json.loads(res.text)
        # 回复给好友
        return dict['showapi_res_body']['text']

if __name__ == '__main__':
    itchat.auto_login()

    # 获取自己的UserName
    myUserName = itchat.get_friends(update=True)[0]["UserName"]
    itchat.run()