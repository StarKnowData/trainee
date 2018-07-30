# orangescrum in windows

### 环境

- Apache 2.4.33
- PHP 5.6.36
- mysql 5.7

### 使用工具：[XAMPP](https://www.apachefriends.org/zh_cn/index.html)

### 最终结果

![](win.gif)

### 步骤

**1.创建虚拟主机。** 我把文件放在了虚拟机的C:\orangescrum中，根目录在C:\orangescrum\app\webroot。

1.1 在实际主机上的hosts文件中加上虚拟主机域名与ip地址

    172.29.214.88 www.orangewin.com

1.2 修改虚拟机上Apache的配置文件httpd.conf以及\extra\httpd-vhosts.conf

httpd.conf中取消以下的注释，将httpd-vhosts.conf文件导入虚拟主机配置：

    Include conf/extra/httpd-vhosts.conf 
 
在httpd-vhosts.conf文件中进行配置信息修改

 
    <VirtualHost *:80>
	    ServerAdmin webmaster@dummy-host.example.com
	    DocumentRoot "C:\orangewin\app\webroot"  //站点根目录
	    ServerName www.orangewin.com			 //绑定的域名
	    <Directory "C:\orangewin\app\webroot">	 //对根目录的一些权限设置
		    SetOutputFilter DEFLATE
		    Options FollowSymLinks ExecCGI
		    Require all granted
		    AllowOverride All					//方便启动mod_rewrite
		    Order allow,deny
		    Allow from all
		    DirectoryIndex index.html index.php
	    </Directory>
    </VirtualHost>

配置完后就可在实际主机上访问了。

**2.按照安装向导进行操作。** 类似在ubantu上的操作，默认已经关闭了mysql的严格模式。

> XAMPP默认phpMyAdmin的初始用户有root，密码为空
