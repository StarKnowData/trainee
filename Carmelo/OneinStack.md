# OneinStack

- [简介](#简介)
- [安装](#安装)
- [卸载](#卸载)
- [版本更新](#版本更新)
- [备份](#备份)
- [创建与删除虚拟主机](#创建与删除虚拟主机)
- [管理服务](#管理服务)


### 简介

一键安装或者卸载环境组合，适用于 linux 系统

下载地址：[https://oneinstack.com/download/](https://oneinstack.com/download/)

> 以下所有的操作 (*除了管理服务*) 需要首先进入到 oneinstack 文件夹中


### 安装

按照官方文档即可，官方操作文档：[https://oneinstack.com/install/](https://oneinstack.com/install/)

    sudo chmod + x ./install.sh 赋予文件可执行权限

**1.** 进入 oneinstack 文件

**2.** 获得权限，运行 **install.sh** 文件进行安装自己所需要的环境

![](https://github.com/UncleLincoln/trainee/tree/master/Carmelo/images/oneinstack/OneinStack_first.gif)

**3. 安装中**

![](https://github.com/UncleLincoln/trainee/tree/master/Carmelo/images/oneinstack/OneinStack_installing.gif)

**4. 安装完成**

![](https://github.com/UncleLincoln/trainee/tree/master/Carmelo/images/oneinstack/OneinStack_finsh.gif)

### 卸载

执行 **uninstall.sh** 文件即可

![](https://github.com/UncleLincoln/trainee/tree/master/Carmelo/images/oneinstack/OneinStack_uninstall.png)

### 版本更新

执行 **upgrade.sh** 文件即可

![](https://github.com/UncleLincoln/trainee/tree/master/Carmelo/images/oneinstack/OneinStack_update.png)

### 备份

执行 **backup_setup.sh** 文件即可，可以对数据库或者网站数据进行本地备份或者云备份。

### 创建与删除虚拟主机

**添加**：

1. 修改 /etc/host 文件，添加一个虚拟主机的对应域名绑定一个 ip（虚拟机的 IP 地址）
2. 执行 `vhost.sh` 文件，按提示操作,会提示启动 Apache 等服务器服务，启动后出现以下画面表示配置成功
![](https://github.com/UncleLincoln/trainee/tree/master/Carmelo/images/oneinstack/OneinStack_Run_Vhost.png)
3. 如果在 windows 上想要访问该虚拟主机的话，建议virtualbox的该虚拟机的网络配置改为**桥接网络**，在虚拟机中通过 `ifconfig` 可以查看分配给虚拟机的 IP 地址，再修改本地的 hosts 文件即可通过浏览器访问虚拟主机。
    

**删除**

执行以下语句
    
    ./vhost.sh del

### 管理服务

详见: [https://oneinstack.com/install/](https://oneinstack.com/install/)

基本上都是以下格式：

    service 服务名称 {start|stop|restart|reload|status}

**使用 mysql 数据库**

开启服务后：

    $ mysql -u 用户名 -p 密码

创建数据库并设置字符集以及排序规则，例如：

     create database orangescrum default character set utf8 collate utf8_unicode_ci

删除数据库，例如：

    drop database orange





