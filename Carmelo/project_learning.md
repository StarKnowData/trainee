# 项目学习 （一）

- [学习目的](#学习目的)
- [项目链接](#项目链接)
- [项目分析](#项目分析)
- [学习收获](#学习收获)

## 学习目的

这次学习的主要目的是对前后端分离的软件设计模式，以及对后端的部署能有初步的整体认识。

在此选择两个带后端的小程序项目进行学习。以下是个人在学习过程中的一些见解，若有不足之处请各位指出，会加以深刻反思，继续努力学习。

## 项目链接

- [https://github.com/RangerGuan/geekland](https://github.com/RangerGuan/geekland)
- [https://github.com/vincenth520/pinche_xcx_data](https://github.com/vincenth520/pinche_xcx_data)

在此对项目的作者表示深深的感谢。

## 项目分析

- [极客社区](#极客社区)
- [同城拼车](#同城拼车)

这里选择的小程序都是带后台的。小程序相当于前端的展示，有着一定的框架，主要由 `wxml,wxss,js,json` 文件组成，支持 `json` 格式的数据。

小程序中：

- wxml：类似于 html
- wxss：类似于 css
- js：用于页面的逻辑处理
- json：配置文件

详情请参考小程序 [官方文档](https://developers.weixin.qq.com/miniprogram/dev/)

### 极客社区

##### 简要

该项目服务端使用了 `WordPress` 。因此改后台可以对应到多个前端，包括小程序、web端等。

我服务端使用的环境：

- linxu ( ubantu )
- Apache
- mysql
- php

##### 安装部署

按照作者的提供的**使用**提示进行安装

**1. 服务端配置**

- 创建虚拟主机 
- 将 server 目录下文件导入虚拟主机的目录中
- 创建数据库 WordPress（自定义名字，用于配置 WordPress ），并按要求修改 sql 文件中的域名为自己服务器的域名并导入数据进入数据库。

我选择的是使用本地测试，为了绕过微信开发的 https 验证，可以使用 [ngrok](https://ngrok.com/) 进行测试。使用如下语句（填上你的虚拟主机域名，所在服务端口）即可开启 ngrok 服务进行测试。

> 缺点：每次关闭服务或者由于其他网络原因造成关闭后再次开启 ngrok 服务都会重新分配一个地址。

    ./ngrok http -host-header=domain port

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/learning_demo/ngrok.gif)

**2. 小程序端配置**

- 导入项目
- 修改 `app.js` 的 `serverUrl` 为服务器的地址即可

**3. 部署完成**

小程序:

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/learning_demo/mini.gif)

web端：

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/learning_demo/web.gif)

##### 分析

在看完了源码后，基本了解了前后端的结构，后台使用了 [WordPress](https://codex.wordpress.org/Main_Page)，关于 WordPress 的这里就不细说了，可以用来搭建博客等，也可以像这里一样把它作为后台，由前端的小程序通过 https 向服务器发送请求返回数据，服务端响应的返回的将是 json 数据

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/learning_demo/url.png)

	APP/
	  |- images/							# 存放 tabBar 的文件
		  |- ...
	  |- pages
		  |- detail						# 显示单篇文章内容的页面相关文件
			  |- detail.js
			  |- detail.json
			  |- detail.wxml
			  |- detail.wxss
		  |- index						# 首页页面的相关文件
			  |- ...						
		  |- theme						# 主题页面相关文件（包括 development、 intelligent、 intnet 页面）
	  |- utils
		  |- util.js						# 关于时间转换分离的逻辑处理
	  |- vender
		  |- weui
			  |- ...					# 样式依赖
		  |- wxParse
			  |- ...					# 处理文件格式解析等 （提供了将 html 类型的文件转换为纯文本的 wxPares 方法等）
	  |- app.js							# 全局逻辑
	  |- app.json							# 全局配置
 	  |- app.wxss							# 全局样式
	  |- project.config.json 					# 配置文件

值得学习的几个功能：正在加载、暂无数据、加载更多

前两个功能可以通过设置状态量来决定是否显示“正在加载”、“暂无数据”的字样。“加载更多”则通过往下继续发送请求并且将旧数据与新数据连接起来即可。

/pages/index/index.js

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/learning_demo/function.png)

### 同城拼车

##### 简要

该项目后端使用了是 `ThinkPHP` 框架，实现了诸如发布信息、收藏、点赞、评论等诸多功能。

我服务端使用的环境：同上一个项目环境

##### 安装部署

**1. 服务端配置** 

按照作者的安装向导进行安装，我这里依然选择本地测试，采用 [ngrok](https://ngrok.com/) 进行测试。

- 创建虚拟主机，开启 Apache 服务
- 将后端的文件导入虚拟主机的目录下
- 修改 `config/config-dist.php` 进行数据库配置，并修改 `\Apps\Api\Conf\config.php` 中的内容

**2. 小程序配置**

基本操作同上一个项目，这里是修改 `/utils/util.js` 中的 `rootDocment` 为你的服务器域名

若要实现更改个人信息的头像的操作，还需要将 `/pages/my/info/info.js` 中的 `dateAvatar()` 方法的 `wx.uploadFile({...})` 中的 `url` 修改为你的服务器地址。

**3. 部署完成**

效果图同作者的实例基本一样

##### 分析

**数据库**

	uid，iid，fid，zid， cid 等分别指用户 id，拼车信息 id，收藏 id， 赞 id， 评论 id 等

    user（id, ......,openid,......）  		
										----- 用户信息表
	Info（id, type, uid, see, .....）			
										----- 拼车详情信息表，uid 代表发布该拼车信息的用户
	fav （id, uid, iid, ......）				 
									    	----- 收藏表，指的是某位 user 对某条 info 的收藏
	zan （id, uid, cid, ......）		
										----- 赞表，指的是某位 user 对某 comment 的点赞
	msg （id, uid, content, see, type, fid）
										----- 针对的是消息模块的专用表
	comment（id, uid, iid, type, reply）
										----- 评论信息表，uid 指的是评论发出者，iid 指的是 info/dynamic 的 id，若是回复信息，reply 指的是回复的对象的内容
	dynamic（id, content, zan, uid）
										----- 动态信息表，uid 为发表该动态的用户 id
	appointment（id, uid, iid, ......）   
										----- 预约信息表，uid 为预约发出者，iid 指的是拼车信息 id

可以看到在 msg 表中有一个属性 see：这可以认为是一个状态变量，控制着用户是否收到了新消息的通知动态信息。

**后端具体分析**

应用的主要控制文件在 `Apps` 下的 `Api` 目录下

    	Apps/Api
	  |- Common/							# 整个应用的共用文件
		  |- function.php 
	  |- Conf							# 应用配置文件，配置 appid 等
		  |- ...							
	  |- Controller							# 控制器
		  |- UserController
		  |- UploadController
		  |- MsgController
		  |- InfoController
		  |- FavController
		  |- DynamicController
		  |- CommentController
		  |- AppointmentController						
	  |- Model							# 模型，一般一个数据库对应一个模型，但可根据实际情况而定
		  |- Comment
		  |- Dynamic
		  |- Info
		  |- User

common: function.php（包含整个应用共有的方法）

- vaild_sk($sk)    
验证登陆是否过期 使用了框架的 S 方法（缓存）
- msg($type, $uid, $fid, $content, $url)  
发送消息：对应的是对表 msg 的数据添加
- getToken()   
向微信发送请求获取 openid
- sendMessage($data)  
发送消息，值得是收到赞、评论等信息时发出的通知信息
- http_post_data($url, $data_string)

Model:

- Comment: 添加评论、获取评论
- Dynamic：添加动态信息
- Info: 添加订单信息，获取订单信息
- User: 获取用户 id 或者是 openid

Controller

**1. UserController**

- login()	
- editUser() 

   		修改成功将返回给前端的 json 数据包含：状态代码、状态信息、更新的用户信息

**2. UploadController**

使用 ThinkPHP 框架中的 upload 类进行上传图片操作

源码文件位于：`\ThinkPHP\Library\Think\Upload.class.php`

**3. NoticeController**

负责处理的是 “免责声明” 部分

index()：将会在 `/pages/notice/index.js` 中发送请求

index()：从数据库在的 notice 表中按照 id 值进行查找，成功后将会向前端返回 json 数据

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/learning_demo/notice.png)

**4. MsgController**

主要负责的是 `/pages/msg/index` 的页面向后端发送的请求

getAll():按照 msg 的 type 类型进行分类查询前端**未读取过的新消息**（判断值是 `see` 属性的值是否为0），并给出各自分类的条数

get():获取与当前用户有关的消息，并且设置为全部信息已读，并将符合的消息返回给前台

**5. InfoController**

> 需要了解 `addInfo` 、 `getInfo` 方法操作数据库

对发布的订单的增添、修改、删除操作以及展示列表信息等

add()：添加或者修改信息到数据库表 info 中，在小程序中一个完整的添加发送的请求顺序为:

/info/add --> /fav/isfav（是否收藏） --> /info/index （获取新添加的发布信息）--> /comment/get_count（获取评论总数） --> /comment/get （获取评论）

index()：查询 Info 表获取该用户特定id的信息

lists(): 对应于 `/pages/index/index` 等要列出相关的info的页面，没有进行错误处理

mylist(): 获取与当前用户有关的 info 列表

mycount():获取与当前用户有关的 info 列表的数目

**6. FavController**

表 `Fav` 中的 `iid` 对应的是info的 `id`

（iid由前端传入）

myFav(): 当前用户的收藏的 info 列表 

isFav(): 判断某条 info 是否被收藏

delFav(): 取消某条 info 的收藏

addFav(): 对某条 info 进行收藏

**7. DynamicController**

获得动态类别、对动态的增、删、改操作，和对 info 的操作相似。

**8. CommentController**

get():获取评论

get_count():获取评论数目

add()：添加评论，同时判断评论者与被评论者是否相同，决定是否发送提醒消息

zan()：点赞操作，分为自己点赞以及别人给你点赞的情况，与 add() 操作基本一样

**9. AppointmentController**

my():获取我的预约

add()：添加动态

del():删除动态

getList():获得动态列表

> 需要了解 I 方法

##### ThinkPHP

curd 操作数据库：[data](http://www.thinkphp.cn/info/323.html)

框架函数用法: [ACDFMLSRUI](https://www.kancloud.cn/curder/php/123665)

框架介绍：
 
- [https://github.com/top-think](https://github.com/top-think)

- [http://www.dwenzhao.cn/profession/language/thinkphp.html](http://www.dwenzhao.cn/profession/language/thinkphp.html)

- [https://blog.csdn.net/m0_37645820/article/details/79009990](https://blog.csdn.net/m0_37645820/article/details/79009990)

模型类是与表相对应的

模型类：定义特殊的业务逻辑  

##### 微信小程序用户登录以及验证流程

[https://www.jianshu.com/p/c5f6c98b2685](https://www.jianshu.com/p/c5f6c98b2685)

**功能学习：**

发送消息提醒功能，对应的是 `function.php` 中的 `msg()` 方法，与 `MsgController` 。

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/learning_demo/msg.png) 

**遇到的问题**

- 1. 路由功能

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/learning_demo/pincheone.png)

将小程序中的地址更换后看到 `ngrok` 服务出现以上画面，显示 404，我被这个问题困扰了挺久的，后来发现引起这个原因的很可能与 `ThinkPHP` 框架的路由功能有关，按理说替换了地址应该就可以了，这里出现问题可能和我的 Apache `mod_rewrite` 重写模块未能起作用有关。看了 `index.php` 中目录应用定义后，`ThinkPHP` 中关于路由功能有几种使用方式，这里将 `rootDocment` 改为：

    https://fa2185e1.ngrok.io/index.php/api/

也可以解决了问题。

- 2. 动态页面未能正常显示

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/learning_demo/pinchetwo.png)

遇到这个问题的时候，应该这样考虑，到底是前端出错了还是后端未能正常返回数据，一步步来分析问题出现的原因，我们首先假定后端未能正确返回数据，先检查下后端能否返回正常的数据，如果后端没有问题，能正常返回数据，则问题出现在前端小程序的逻辑上。

在这里检测后端能否正常返回数据，可以使用 [postman](https://www.getpostman.com/) 进行检查。

我们找到小程序动态页面请求的后端服务方法 DynamicController 中的 getList() 进行调试。 

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/learning_demo/sql.png)

我们依次使用 73、74 行中的语句进行调试，查看到底是哪个地方有问题，在 `postman` 中进行请求查看能否返回正常的 `json` 数据。

最后我们发现所有的 sql 语句都没有问题，但是到了 82 行以后的 `$result` 变量出现问题了，我们输出 `$result` 变量是可以得到正常的数据的，但是进行 `exit(json_encode($result));` 语句进行转换为 json 数据后该变量就无法输出了。

因此问题出现在 `exit(json_encode($result));` 中，我们猜想可能是由于服务端的编码的问题出错，将 84 行的‘获取成功’改为英文的 ‘success’ 后，问题解决了。

- 3. 图片上传失败问题

按照 UploadController 文件中定义的，上传文件目录在根目录下的 Uploads 文件夹中，若没有就创建一个。

需要给这个文件夹写入的权限，否则无法上传。

    chmod -R 777 your Uploads path


**增加功能**

在读完后台源码后，尝试修改源码，添加了点赞取消功能。

在 CommentController 中加入函数 zan() 中添加以下代码即可

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/learning_demo/zan.png)
 
## 学习收获

通过这两个项目的学习，收获颇多。

第一个项目主要学习小程序的 `js` 逻辑，第二个项目注重学习了后端的功能实现。在前后端分离的结构中，前端与后端的通信通常是由前端通过向后端发送 `http` 请求获取比如 json 等符合的数据类型。比如拼车项目中：

前端小程序发送 （这个地址的后端请求了控制器中的 UserController 的 vaild_sk() 方法）

    https://324202e1.ngrok.io/index.php/api/user/vaild_sk

后端完成一个请求后返回 json 数据

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/learning_demo/Hou.png)

在调试的过程中，当程序出现问题了，需要学会判断问题出现在哪里，可以从前端与后端分别考虑，确定问题出现的具体位置到底是前端的处理，还是后端的处理上，这里可以使用 [postman](https://www.getpostman.com/) 来进行后端的接口测试，测试是否能返回需要的数据类型。

还了解一些 `php` 知识，以及 `ThinkPHP` 框架的使用。







