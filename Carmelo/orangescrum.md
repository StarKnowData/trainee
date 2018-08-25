# orangescrum

项目地址: [orangescrum](https://github.com/Orangescrum/orangescrum)

- [安装及要求](#安装及要求)
- [安装总结](#安装总结)
- [orangescrum_in_Windows](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/orangescrum_in_window.md)


### 安装及要求

环境要求：

- Apache（启动 `mod_rewrite` ）
- mysql 至少 5.3 版本以上
- php 至少 5.3 以上，最好 7 以下
- 关闭 mysql 的严格模式

步骤：

- 创建虚拟主机
- 克隆项目到工作目录中
- 浏览器访问虚拟主机，按照提示操作

使用的环境：

-  Apache 2.4
-  Nginx 1.41
-  php 5.6
-  mysql 5.7

安装完成后的样子：

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/orangescrum/get.gif)

### 安装总结

1.  虚拟主机的使用
2.  phpMyAdmin 操作数据库
1.  查看错误日志分析存在的错误问题
2.  通过 Chrome 的检查解决图片问题
1.  根据 Apache 或者 Nginx 的状态查找错误的地方
1.  lnmp 一键安装配置环境下 mysql 5.7 的严格模式的关闭
1.  学到的一些的 linux 操作以及其他知识

#### 1. 虚拟主机的使用

**步骤：**

1. virtualbox 中该虚拟机的网络连接方式选择 **桥接网卡**（当然还有其他方式）以获得分配的 ip 地址，此时实际主机可以和虚拟机进行互 ping
2. Oneinstack 中执行 `./vhost.sh` 文件创建虚拟主机
3. 修改 hosts 文件，我用的是 Windows 操作系统，文件在 \Windows\System32\drivers\etc ，添加虚拟主机的域名以及其绑定的 ip 地址，比如：我的虚拟机获得的 IP 是192.168.0.101，虚拟主机的 domain 是 www.orangelcan.com，则将这组对应添加到 hosts 文件中

	`192.168.0.101 www.orangetest.com`

4. 完成前面三步后，就可以通过 Windows 上的浏览器访问虚拟机的 ip 及虚拟主机了。如图：

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/orangescrum/orangescrum_01.png)

按提示给予相应文件写的权限后就可以看到安装提示了

    cd  /data/wwwroot/www.orangetestone.com/app
    chmod -R 0777 Config/*
    chmod -R 0777 tmp/*
    chmod -R 0777 webroot/*

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/orangescrum/orangescrum_02.png)


> 一个 ip 可以绑定多个域名，但是一个域名只能绑定一个 ip 。


#### 2.  phpMyAdmin

访问：虚拟机 ip/phpMyAdmin  	

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/orangescrum/phpMyAdmin.gif)

#### 3. 查看错误日志分析存在的错误问题

###### 3.1 案例一 

找到虚拟主机的错误的日志存放位置：（以我的为例）

    /data/wwwlogs/www.orangetest.com_error_apache_log

可以看到问题出现的原因，然后就可以根据出现的问题去寻找解决的方案。

###### 3.2 案例二

网页中出现如下问题：`database connection`

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/orangescrum/database.png)

我们可以进入到 /app/Config 中的 tmp 目录下的文件寻找错误原因，我们进入 /tmp 后看到有文件 error.log，存放着数据库连接错误的原因。我们可以看到出现了 `PDOException: SQLSTATE[HY000]: General error: 3065` 此类错误。

寻找解决方案后，觉得有可能是 mysql 的严格模式未关闭所致，因此尝试关闭严格模式，重启 mysql，发现新大陆，问题解决。

#### 4. 通过 Chrome 的检查解决图片问题

出现了图片损坏情况如图：

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/orangescrum/Imagelost.png)

通过 chrmoe 的检查可见，css 等文件找不到，这可能是因为根目录位置不对所致的。

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/orangescrum/Imagelost_1.png)

后来我们发现 css 等文件在 /app/webroot 目录下，因此依次把在 Nginx 和 Apache 配置中的站点的根目录修改至 /app/webroot，图片问题得到解决。

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/orangescrum/web1.png)

nginx配置图略

但是 sign up下边的破损图片仍然未解决，从 Chrome 看出地址这个地方出错了 `@SUB_FOLDER`

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/orangescrum/web3.png)

我们再来看看该工作目录下的错误日志文件，在 `app/tmp/logs` 目录下的 `error.log` 中有记录。

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/orangescrum/web4.png)

我们看到了问题就是出在 `@SUB_FOLDER` 上，查阅了相关资料后，找到了修改的方法，`@SUB_FOLDER` 出现在 `app/Config/constants.php` 中。我们对 `constants.php` 做出以下修改即可解决问题。

    define('SUB_FOLDER', '@SUB_FOLDER');  修改为  define('SUB_FOLDER', '/');

#### 5. 查看Apache或者Nginx的状态查找错误的地方

    service httpd status
    service Nginx status

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/orangescrum/web.png)

看到问题出现所在，文件夹不存在，很明显根目录写错了。那么我们把它写对之后，在重启下 Nginx 和 Apache ，好的问题解决了。

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/orangescrum/Imagefound.png)

#### 6. lnmp 一键安装配置环境下 mysql 5.7 的严格模式的关闭

关闭 mysql 的严格模式，一般是在 `/etc/my.cnf` 中进行更改，但是这对于使用 lnmp 一键安装的方式配置的环境而言，有可能会不起作用，那么我们可以通过在 `/usr/local/mysql/my.cnf` 中进行更改，如果在 `/usr/local/mysql` 中没有 `my.cnf` 文件，则新创建一个 `my.cnf` 文件，并写入以下语句：

    [mysqld]
    sql_mode = NO_ENGINE_SUBSTITUTION

之后重启 mysql 即可



#### 7. 学到的一些的 linux 操作以及其他知识

添加权限：

	chmod  -权限类型（rwf） XXX filename/

直接将 root 全部权限交给了用户，进而该用户可以操作具有 root 权限的操作

	sudo su

vim 中编辑文件：

	?field 搜索关键字段

清空文件内容：

	echo "" > file

mysql 中 datatime 类型的取值范围：

	1000-01-01 00:00:00 到 9999-12-31 23:59:59





