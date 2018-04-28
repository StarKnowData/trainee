Python SMTP发送邮件
===============

 SMTP（Simple Mail Transfer Protocol）即简单邮件传输协议,它是一组用于由源地址到目的地址传送邮件的规则，由它来控制信件的中转方式。

 python的smtplib提供了一种很方便的途径发送电子邮件。它对smtp协议进行了简单的封装。

 Python创建 SMTP 对象语法如下：

 
```

import smtplib

smtpObj = smtplib.SMTP( [host [, port [, local_hostname]]] )

```

 参数说明：

  *  host: SMTP 服务器主机。 你可以指定主机的ip地址或者域名如: runoob.com，这个是可选参数。 
*  port: 如果你提供了 host 参数, 你需要指定 SMTP 服务使用的端口号，一般情况下 SMTP 端口号为25。 
*  local\_hostname: 如果 SMTP 在你的本机上，你只需要指定服务器地址为 localhost 即可。 
 Python SMTP 对象使用 sendmail 方法发送邮件，语法如下：

 
```

SMTP.sendmail(from_addr, to_addrs, msg[, mail_options, rcpt_options])

```

 参数说明：

  *  from\_addr: 邮件发送者地址。 
*  to\_addrs: 字符串列表，邮件发送地址。 
*  msg: 发送消息 
 这里要注意一下第三个参数，msg 是字符串，表示邮件。我们知道邮件一般由标题，发信人，收件人，邮件内容，附件等构成，发送邮件的时候，要注意 msg 的格式。这个格式就是 smtp 协议中定义的格式。

 ### 实例

 以下执行实例需要你本机已安装了支持 SMTP 的服务，如：sendmail。

 以下是一个使用 Python 发送邮件简单的实例：

  实例
--

 <pre>

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender = 'from@runoob.com'
receivers = ['429240967@qq.com'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
# 三个参数：第一个为文本内容，第二个 plain 设置文本格式，第三个 utf-8 设置编码
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] =  Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
try:
    smtpObj = smtplib.SMTP('localhost')
smtpObj.sendmail(sender, receivers, message.as_string())
print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
</pre>

 我们使用三个引号来设置邮件信息，标准邮件需要三个头部信息： **From**, **To**, 和 **Subject** ，每个信息直接使用空行分割。

 我们通过实例化 smtplib 模块的 SMTP 对象 *smtpObj* 来连接到 SMTP 访问，并使用 *sendmail* 方法来发送信息。

 执行以上程序，如果你本机安装 **sendmail（邮件传输代理程序）**，就会输出：

 
```

$ python test.py 
邮件发送成功

```

 查看我们的收件箱(一般在垃圾箱)，就可以查看到邮件信息：

 ![](http://www.runoob.com/wp-content/uploads/2016/04/smtp1.jpg)


 如果我们本机没有 sendmail 访问，也可以使用其他邮件服务商的 SMTP 访问（QQ、网易、Google等）。

  实例
--

 <pre>

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
# 第三方 SMTP 服务
mail_host="smtp.XXX.com" #设置服务器
mail_user="XXXX" #用户名
mail_pass="XXXXXX" #口令 
sender = 'from@runoob.com'
receivers = ['429240967@qq.com'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] =  Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
try:
    smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 25) # 25 为 SMTP 端口号
smtpObj.login(mail_user,mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
</pre>

  使用Python发送HTML格式的邮件
-------------------

 Python发送HTML格式的邮件与发送纯文本消息的邮件不同之处就是将MIMEText中\_subtype设置为html。具体代码如下：

  实例
--

 <pre>

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.header import Header
sender = 'from@runoob.com'
receivers = ['429240967@qq.com'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">这是一个链接</a></p>
"""
message = MIMEText(mail_msg, 'html', 'utf-8')
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] =  Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
try:
    smtpObj = smtplib.SMTP('localhost')
smtpObj.sendmail(sender, receivers, message.as_string())
print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
</pre>

  执行以上程序，如果你本机安装sendmail，就会输出：

 
```

$ python test.py 
邮件发送成功

```

 查看我们的收件箱(一般在垃圾箱)，就可以查看到邮件信息：

 ![](http://www.runoob.com/wp-content/uploads/2016/04/smtp2.jpg)


  Python 发送带附件的邮件
---------------

 发送带附件的邮件，首先要创建MIMEMultipart()实例，然后构造附件，如果有多个附件，可依次构造，最后利用smtplib.smtp发送。

  实例
--

 <pre>

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
sender = 'from@runoob.com'
receivers = ['429240967@qq.com'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] =  Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
#邮件正文内容
message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))
# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('test.txt', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)
# 构造附件2，传送当前目录下的 runoob.txt 文件
att2 = MIMEText(open('runoob.txt', 'rb').read(), 'base64', 'utf-8')
att2["Content-Type"] = 'application/octet-stream'
att2["Content-Disposition"] = 'attachment; filename="runoob.txt"'
message.attach(att2)
try:
    smtpObj = smtplib.SMTP('localhost')
smtpObj.sendmail(sender, receivers, message.as_string())
print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
</pre>

 
```

$ python test.py 
邮件发送成功

```

 查看我们的收件箱(一般在垃圾箱)，就可以查看到邮件信息：

 ![](http://www.runoob.com/wp-content/uploads/2013/11/smtp3.jpg)


 在 HTML 文本中添加图片
--------------

 邮件的 HTML 文本中一般邮件服务商添加外链是无效的，正确添加突破的实例如下所示：

  实例
--

 <pre>

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
sender = 'from@runoob.com'
receivers = ['429240967@qq.com'] # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
msgRoot = MIMEMultipart('related')
msgRoot['From'] = Header("菜鸟教程", 'utf-8')
msgRoot['To'] =  Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
msgRoot['Subject'] = Header(subject, 'utf-8')
msgAlternative = MIMEMultipart('alternative')
msgRoot.attach(msgAlternative)
mail_msg = """
<p>Python 邮件发送测试...</p>
<p><a href="http://www.runoob.com">菜鸟教程链接</a></p>
<p>图片演示：</p>
<p><img src="cid:image1"></p>
"""
msgAlternative.attach(MIMEText(mail_msg, 'html', 'utf-8'))
# 指定图片为当前目录
fp = open('test.png', 'rb')
msgImage = MIMEImage(fp.read())
fp.close()
# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<image1>')
msgRoot.attach(msgImage)
try:
    smtpObj = smtplib.SMTP('localhost')
smtpObj.sendmail(sender, receivers, msgRoot.as_string())
print "邮件发送成功"
except smtplib.SMTPException:
    print "Error: 无法发送邮件"
</pre>

  
```

$ python test.py 
邮件发送成功

```

 查看我们的收件箱(如果在垃圾箱可能需要移动到收件箱才可正常显示)，就可以查看到邮件信息：

 ![](http://www.runoob.com/wp-content/uploads/2016/04/smtp4.jpg)


  使用第三方 SMTP 服务发送
---------------

 这里使用了 QQ 邮箱(你也可以使用 163，Gmail等)的 SMTP 服务，需要做以下配置：

 ![](http://www.runoob.com/wp-content/uploads/2014/01/qqmail-set2.jpg)


 QQ 邮箱通过生成授权码来设置密码：

 ![](http://www.runoob.com/wp-content/uploads/2014/01/qqmail-set.jpg)


 QQ 邮箱 SMTP 服务器地址：smtp.qq.com，ssl 端口：465。

 以下实例你需要修改：发件人邮箱（你的QQ邮箱），密码，收件人邮箱（可发给自己）。

  QQ SMTP
-------

 <pre>

#!/usr/bin/python
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
my_sender='429240967@qq.com' # 发件人邮箱账号
my_pass = 'xxxxxxxxxx' # 发件人邮箱密码
my_user='429240967@qq.com' # 收件人邮箱账号，我这边发送给自己
def mail():
    ret=True
try:
        msg=MIMEText('填写邮件内容','plain','utf-8')
msg['From']=formataddr(["FromRunoob",my_sender]) # 括号里的对应发件人邮箱昵称、发件人邮箱账号
msg['To']=formataddr(["FK",my_user]) # 括号里的对应收件人邮箱昵称、收件人邮箱账号
msg['Subject']="菜鸟教程发送邮件测试" # 邮件的主题，也可以说是标题
server=smtplib.SMTP_SSL("smtp.qq.com", 465) # 发件人邮箱中的SMTP服务器，端口是25
server.login(my_sender, my_pass) # 括号中对应的是发件人邮箱账号、邮箱密码
server.sendmail(my_sender,[my_user,],msg.as_string()) # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
server.quit() # 关闭连接
except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
ret=False
return ret
ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")
</pre>

  
```

$ python test.py 
邮件发送成功

```

 发送成功后，登陆收件人邮箱即可查看：

 ![](http://www.runoob.com/wp-content/uploads/2013/11/423C9FDF-EBC5-4115-8D16-0046B5E05DBC.jpg)


 更多内容请参阅：<https://docs.python.org/2/library/email-examples.html>。
