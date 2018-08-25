# summary

- [问题解决](#问题解决)
- [知识积累](#知识积累)
- [问题积累](#问题积累)
- [常用工具](#常用工具)

## 问题解决

当出现问题时，应该冷静，学会查看日志，结合工具进行排查，确定问题出现的地方，善于运用网络搜素。

### 一 使用 Chrome 检查

web 页面会遇到各种各样的问题，比如图片加载失败，资源不显示等，这类问题我们可以尝试使用 Chrome 的检查功能进行检查（右击鼠标选择检查即可看见），Chrome 提供了许多可以调试的工具，network 可以查看对接口的请求情况等。

### 二 使用 Postman 检查接口请求是否有效

当我们发现某条请求出现了问题了，我们可以通过 Chrome 或者其他方式得到一些 Headers、 body 等信息，我们可以在 [postman](https://www.getpostman.com/) 中对该接口配上得到的   Headers、body 等信息**逐步添加**的进行请求，来确定是否有效，问题出现的地方在哪里，是缺少了参数还是其他原因。

### 三 查看错误日志

错误日志是很重要的，常常又是容易忽略的，当我们看到一堆错误的时候，可能无从下手，但是通过查看服务器端的错误日志可能会有意外的发现。比如我最近经常接触到的 Apache、Nginx、vhost 的 `error.log` 。有时候我们调试的时候想看见最新的错误，看最近的一次错误时，可以将 `error.log` 的信息进行清空处理，在进行调试。

常用命令： `echo '' > error.log`

### 四 确定问题出错地方

有的时候我们遇到问题，习惯了在不清楚问题所在的时候就瞎找，以至于耗费了大段的时间也无济于事。所以确定问题所在的地方十分重要。在前后端分离的项目中，寻找问题的思路应该是分为前端和后端两部分，后端需要检查的是提供给前端的接口能否正确返回前端需要的格式的数据，在能正确返回的情况下，应该检查前端的逻辑处理是否有问题。

前后端之间通常通过发送 `http` 请求的形式进行通信，因此对接口的调试十分重要，[postman](https://www.getpostman.com/) 可以说是很好的工具。

## 知识积累

- [前后端](#前后端)
- [路由](#路由)
- [虚拟主机](#虚拟主机)
- [框架应用](#框架应用)
- [node](#node)

这些天的研究学习，接触了几个包含前后端的项目，对一个项目的开发、部署有了一定的整体的了解。

##### 前后端

前端接收到用户的请求信息，通过向后端发送 http 请求向后端发送处理信息，后端进行完复杂的业务逻辑处理后，返回一定格式的数据（json、xml 等）给前端。前端进行一定的数据处理后将其展示出来，这就是我们常说的 view 。而后端一般包含 controller、model 等。

##### 路由

这个是我之前比较不熟悉的点。路由、具体处理程序、服务端、前端他们之间的关系，在我看了 [node入门](https://www.nodebeginner.org/index-zh-cn.html#conclusion-and-outlook) 后有了一定的清晰认识。虽然这本书讲的是关于 node 的，但是我认为在其他语言里仍然有效。

前端通过 https 向后端发送请求，请求处理相关业务，而为了使得结构更加清晰，访问的 url 能更加明确，路由在这里就起着非常重要的作用了。他规定了收到的请求处理应该交给哪些具体的处理程序进行处理。在 node 中，server 端主入口接收到了请求处理，交由路由进行分配具体的处理程序，具体的处理程序处理完请求后将返回到路由，路由再返回给  server 端主入口进行对前端的输出。

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/summary/route.png)

详情例子请参考：[node入门](https://www.nodebeginner.org/index-zh-cn.html#conclusion-and-outlook) 

##### 虚拟主机

###### 介绍

维基百科的定义：[虚拟主机](https://zh.wikipedia.org/wiki/%E8%99%9A%E6%8B%9F%E4%B8%BB%E6%9C%BA)

一种在单一主机或主机群上，实现多网域服务的方法，可以运行多个网站或服务的技术。虚拟主机之间完全独立，并可由用户自行管理，虚拟并非指不存在，而是指空间是由实体的服务器延伸而来，其硬件系统可以是基于服务器群，或者单个服务器。

web 服务，进行访问实际上是对某个 ip 的主机上的某个端口上的服务进行访问，具体而言就是访问该 ip 下的该端口下的服务，指的是某个文件目录。我们访问不同的域名或者端口就可实现对不同网站的访问，这可以是同一主机，也可以是不同主机的服务。当我们希望我们服务器主机上的两个服务可以都被访问到，这时候就可以创建虚拟主机完成任务。

> 一个 ip 可以对应多个域名，但是一个域名只能对应一个 ip，不同域名对应的其 ip 主机上的服务一般不同。

###### 类型:

- 基于域名
- 基于端口
- 基于 ip

以创建 Apache 虚拟主机为例：

###### 一 基于域名: 

1. 在实际主机上的 hosts 文件中加上虚拟主机域名与 ip 地址

    `172.29.214.88 www.orangewin.com`

1. 修改虚拟机上 Apache 的配置文件 `httpd.conf` 以及 `\extra\httpd-vhosts.conf`
`httpd.conf` 中取消以下的注释，将 `httpd-vhosts.conf` 文件导入虚拟主机配置

	`Include conf/extra/httpd-vhosts.conf` 
 
	在 `httpd-vhosts.conf` 文件中进行配置信息修改

	    <VirtualHost *:80>
		    ServerAdmin webmaster@dummy-host.example.com
		    DocumentRoot "C:\orangewin\app\webroot"  //站点根目录
		    ServerName www.orangewin.com			 //绑定的域名
		    <Directory "C:\orangewin\app\webroot">	 //对根目录的一些权限设置
			    SetOutputFilter DEFLATE
			    Options FollowSymLinks ExecCGI
			    Require all granted
			    AllowOverride All					//方便启动 mod_rewrite
			    Order allow,deny
			    Allow from all
			    DirectoryIndex index.html index.php
		    </Directory>
	    </VirtualHost>

3. 配置完后即可通过访问 www.orangewin.com 请求到该虚拟主机 80 端口的服务。

###### 二 基于端口:

    <VirtualHost *:88>							 // 修改为 88 端口
	    ServerAdmin webmaster@dummy-host.example.com
	    DocumentRoot "C:\orangewin\app\webroot"  //站点根目录
	    ServerName www.orangewin.com			 //绑定的域名
	    <Directory "C:\orangewin\app\webroot">	 //对根目录的一些权限设置
		    SetOutputFilter DEFLATE
		    Options FollowSymLinks ExecCGI
		    Require all granted
		    AllowOverride All					//方便启动 mod_rewrite
		    Order allow,deny
		    Allow from all
		    DirectoryIndex index.html index.php
	    </Directory>
    </VirtualHost>

此外实现需要修改，`httpd.conf` 文件中的监听端口为 88 

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/summary/vhost.png)

配置完后就可在实际主机上访问 12.34.56.78:88 。

###### 三 基于 ip

详情请看参考资料。

参考:[https://www.linuxidc.com/Linux/2016-04/130381.htm](https://www.linuxidc.com/Linux/2016-04/130381.htm)

如果不想自己配置文件进行虚拟主机的创建，[OneinStack](https://oneinstack.com/) 提供了一套创建与删除虚拟主机的[自动方案](https://oneinstack.com/install/)，即为方便。

##### 四 框架应用

看过的几个项目，都应用了不同的框架或者模板，php 开发的后台有用 ThinkPHP 的，也有使用 WordPress 作为后台的，node 开发的有使用 koa，express 的。使用框架可以使得开发更加快捷，高效。也给我日后学习提供了线索，应该熟悉掌握几个框架并能应用。

##### 五 node

两个好用的 node 管理工具: [nvm](https://github.com/creationix/nvm)，[npm](https://github.com/npm/cli)

下载安装：[https://segmentfault.com/a/1190000008653668#articleHeader1](https://segmentfault.com/a/1190000008653668#articleHeader1)

入门解读：[node 入门](https://www.nodebeginner.org/index-zh-cn.html#conclusion-and-outlook)

## 问题积累 

- [MongoDB](#MongoDB)
- [mysql](#mysql)
- [git](#git)
- [权限问题](#权限问题)

### MongoDB

##### 1. 关于 MongoDB 的权限问题 --- code 13 的一些问题：

	MongoDB shell version v4.0.0
	connecting to: mongodb://127.0.0.1:27017
	MongoDB server version: 4.0.0
	> show dbs
	2018-08-24T18:46:48.708+0800 E QUERY    [js] Error: listDatabases failed:{
	        "ok" : 0,
	        "errmsg" : "command listDatabases requires authentication",
	        "code" : 13,
	        "codeName" : "Unauthorized"
	} :
	_getErrorWithCode@src/mongo/shell/utils.js:25:13
	Mongo.prototype.getDBs@src/mongo/shell/mongo.js:65:1
	shellHelper.show@src/mongo/shell/utils.js:865:19
	shellHelper@src/mongo/shell/utils.js:755:15
	@(shellhelp2):1:1

解决办法：赋予用户操作数据库的角色

    ./mongo --yourport 27017 -u "admin" -p "password" --authenticationDatabase "admin"

    如: ./mongo 127.0.0.1 -u 'root' -p --authenticationDatabase admin

	db.grantRolesToUser("admin",["readWrite"])

	用户，角色 （root 权限最强）


参考：[https://stackoverflow.com/questions/23943651/mongodb-admin-user-not-authorized](https://stackoverflow.com/questions/23943651/mongodb-admin-user-not-authorized)

##### 2. 关于开启 auth 模式下连接 MongoDB 数据库的 url 写法：

当我们要连接其他数据库时，而我们的验证是在 admin 中，需要添加 options 项：
`authSource=admin` 。

采用 admin 中的验证连接 MongoDB 操作其他的数据库

	url:'mongodb://username:password@domain:prot/dbname?authSource=admin'
	
	如: url:'mongodb://root:123456@localhost:27017/mall?authSource=admin'

参考：[http://www.voidcn.com/article/p-pbiudstn-bqn.html](http://www.voidcn.com/article/p-pbiudstn-bqn.html)

### mysql

##### 1. 严格模式的关闭

关闭 mysql 的严格模式，一般是在 `/etc/my.cnf` 中进行更改，但是这对于使用 lnmp 一键安装的方式配置的环境而言，有可能会不起作用，那么我们可以通过在 `/usr/local/mysql/my.cnf` 中进行更改，如果在 `/usr/local/mysql` 中没有 `my.cnf` 文件，则新创建一个 `my.cnf` 文件，并写入以下语句：

    [mysqld]
    sql_mode = NO_ENGINE_SUBSTITUTION

之后重启 mysql 即可

##### 2. datatime 类型的取值范围：

	1000-01-01 00:00:00 到 9999-12-31 23:59:59

### git

##### 虚拟机 git clone 项目失败

可能与虚拟机的网络连接状态有关，曾经我使用**桥接网卡**的时候，遇到过这样的问题，但是最后通过修改连接方式为**网络地址转换**，却成功的解决了问题。

### 权限问题

##### 项目图片无法上传等，或者文件无法写入甚至是读取

大多数这个问题与要操作的文件缺少权限有关，比如上传的图片存放的文件没有写入的权限等。此时我们需要给其所缺少的权限。通常使用：

    chmod -R number file

## 常用工具

##### VirtualBox

一款强大的虚拟机软件，可以快捷的创建虚拟机进行各种操作。

下载地址：[https://www.virtualbox.org/wiki/Downloads](https://www.virtualbox.org/wiki/Downloads)

##### MarkdownPad

一款 markdown 编辑器


##### MobaXterm

一款 Windows 上的 ssh 神器，同时支持 ftp、 Rsh、Xdmcp 等多种功能。

下载地址：[http://https://mobaxterm.mobatek.net/download.html](http://https://mobaxterm.mobatek.net/download.html)

##### Postman

强大的 API 调试工具

##### ngrok

一款可以进行内网穿透的软件，可以实现代理到本地的功能。具体使用请参考官网信息。

官网：[https://ngrok.com/](https://ngrok.com/)

##### LNMP 一键安装包

- [OneinStack](https://oneinstack.com/)
- [xampp](https://www.apachefriends.org/zh_cn/index.html)
