# 常用工具

- [MarkdownPad](#MarkdownPad)
- [VitualBox](#VitualBox)
- [MobaXterm](#MobaXterm)
- [Postman](#Postman)

# MarkdownPad

下载安装即可使用

**关于错误：An error occurred with the Html rendering component**

- 需要下载一个插件：[awesomium_v1.6.6_sdk_win](http://markdownpad.com/download/awesomium_v1.6.6_sdk_win.exe)
- 重启 MarkdownPad 即可使用

# VitualBox
VirtualBox 是一款开源虚拟机软件。

- [下载安装](#下载安装)
- [创建虚拟机](#创建虚拟机)
- [快照](#快照)
- [克隆](#克隆)
- [导入与导出](#导入与导出)
- [Ubuntu分区](#Ubuntu分区)
## 下载安装
地址：[https://www.virtualbox.org/](https://www.virtualbox.org/)

## 创建虚拟机

以创建 Windows7 虚拟机为例

**准备材料：**

- [Windows7](https://msdn.itellyou.cn/) 镜像文件
- 安装好的 VitualBox

**步骤：**

1. 修改全局设定。点击管理 --> 全局设定 --> 默认虚拟电脑位置

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/VirtualBox/0.png)
2. 新建 ---> 填写名称、类型

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/VirtualBox/1.png)
3. 分配内存大小

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/VirtualBox/2.png)
4. 选择虚拟硬盘的创建方式

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/VirtualBox/3.png)
5. 选择虚拟硬盘文件类型

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/VirtualBox/4.png)
6. 硬盘分配选择

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/VirtualBox/5.png)
7. 确定硬盘实际大小

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/VirtualBox/6.png)
8. 进入新建虚拟机的设置界面，在系统启动顺序中将**光驱**调到最前的位置

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/VirtualBox/7.png)
9. 在存储中添加准备好的镜像文件

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/VirtualBox/8.png)
10. 设置好后点击启动进入虚拟机,虚拟机上的安装同重装系统一样，按提示操作即可

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/VirtualBox/9.png)

## 快照
**Snapshots**：系统快照，保存虚拟系统在某一时刻的全部运行状态，以后可以将虚拟系统恢复到创建此快照时的状态。在 VirtualBox 中文版中，snapshots 被翻译成“备份”。

**分支快照（branched snapshots）功能**，可以将虚拟系统直接恢复到任意时间的备份，并且保留最近的备份，当修改了过去备份的状态后，可以在原有的备份时间线上创建一个分支，并且可以随时在不同分支上继续运行系统。

## 克隆
语法：`VBoxManage clonehd 需要克隆的虚拟机 vdi 路径 克隆成功后的新的虚拟机 vdi 存放路径 `
> 需要进入到 VirtualBox 的根目录下进行命令行操作。

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/VirtualBox/11.png)

## 导入与导出

**使用场景**

- 需要和别人共享你的 VirtualBox 虚拟机，这样可以省去别人安装虚拟机和配置虚拟机的过程，节省大量时间。
- 当你发现你虚拟机所在的分区没有足够的空间了，你需要把虚拟机转移到另外一个分区上面。

**导出**

1. 点击管理，选择导出虚拟机

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/VirtualBox/1.gif)
2. 按提示操作并勾选勾选“写入 `Manifest` 文件”，在许可栏里可以写入备注信息，最后点击导出

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/VirtualBox/2.gif)
3. 点击导出即可

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/VirtualBox/3.gif)
**导入**

点击管理，选择导入虚拟机，选择之前导出的 `ovi` 文件，即可完成导入

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/VirtualBox/4.gif)

## Ubuntu分区

![](https://github.com/UncleLincoln/trainee/blob/master/Carmelo/images/VirtualBox/10.png)

# MobaXterm

Windows下连接 Linux 的 ssh 工具，同时也支持 ftp 协议，可进行文件传输。除此之外还有许多强大的功能。

# Postman

一个很强大的 API 调试、 Http 请求的工具。通常用于调试接口，测试接口是否有效返回或达到预期的数据或作用。



