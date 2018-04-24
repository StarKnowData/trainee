Python OS 文件/目录方法
=================

**os** 模块提供了非常丰富的方法用来处理文件和目录。常用的方法如下表所示：

序号

方法及描述

1

[os.access(path, mode)](os-access.html)

  
检验权限模式

2

[os.chdir(path)](os-chdir.html)

  
改变当前工作目录

3

[os.chflags(path, flags)](os-chflags.html)

  
设置路径的标记为数字标记。

4

[os.chmod(path, mode)](os-chmod.html)

  
更改权限

5

[os.chown(path, uid, gid)](os-chown.html)

  
更改文件所有者

6

[os.chroot(path)](os-chroot.html)

  
改变当前进程的根目录

7

[os.close(fd)](os-close.html)

  
关闭文件描述符 fd

8

[os.closerange(fd\_low, fd\_high)](os-closerange.html)

  
关闭所有文件描述符，从 fd\_low (包含) 到 fd\_high (不包含), 错误会忽略

9

[os.dup(fd)](os-dup.html)

  
复制文件描述符 fd

10

[os.dup2(fd, fd2)](os-dup2.html)

  
将一个文件描述符 fd 复制到另一个 fd2

11

[os.fchdir(fd)](os-fchdir.html)

  
通过文件描述符改变当前工作目录

12

[os.fchmod(fd, mode)](os-fchmod.html)

  
改变一个文件的访问权限，该文件由参数fd指定，参数mode是Unix下的文件访问权限。

13

[os.fchown(fd, uid, gid)](os-fchown.html)

  
修改一个文件的所有权，这个函数修改一个文件的用户ID和用户组ID，该文件由文件描述符fd指定。

14

[os.fdatasync(fd)](os-fdatasync.html)

  
强制将文件写入磁盘，该文件由文件描述符fd指定，但是不强制更新文件的状态信息。

15

[os.fdopen(fd\[, mode\[, bufsize\]\])](os-fdopen.html)

  
通过文件描述符 fd 创建一个文件对象，并返回这个文件对象

16

[os.fpathconf(fd, name)](os-fpathconf.html)

  
返回一个打开的文件的系统配置信息。name为检索的系统配置的值，它也许是一个定义系统值的字符串，这些名字在很多标准中指定（POSIX.1, Unix 95, Unix 98, 和其它）。

17

[os.fstat(fd)](os-fstat.html)

  
返回文件描述符fd的状态，像stat()。

18

[os.fstatvfs(fd)](os-fstatvfs.html)

  
返回包含文件描述符fd的文件的文件系统的信息，像 statvfs()

19

[os.fsync(fd)](os-fsync.html)

  
强制将文件描述符为fd的文件写入硬盘。

20

[os.ftruncate(fd, length)](os-ftruncate.html)

  
裁剪文件描述符fd对应的文件, 所以它最大不能超过文件大小。

21

[os.getcwd()](os-getcwd.html)

  
返回当前工作目录

22

[os.getcwdu()](os-getcwdu.html)

  
返回一个当前工作目录的Unicode对象

23

[os.isatty(fd)](os-isatty.html)

  
如果文件描述符fd是打开的，同时与tty(-like)设备相连，则返回true, 否则False。

24

[os.lchflags(path, flags)](os-lchflags.html)

  
设置路径的标记为数字标记，类似 chflags()，但是没有软链接

25

[os.lchmod(path, mode)](os-lchmod.html)

  
修改连接文件权限

26

[os.lchown(path, uid, gid)](os-lchown.html)

  
更改文件所有者，类似 chown，但是不追踪链接。

27

[os.link(src, dst)](os-link.html)

  
创建硬链接，名为参数 dst，指向参数 src

28

[os.listdir(path)](os-listdir.html)

  
返回path指定的文件夹包含的文件或文件夹的名字的列表。

29

[os.lseek(fd, pos, how)](os-lseek.html)

  
设置文件描述符 fd当前位置为pos, how方式修改: SEEK\_SET 或者 0 设置从文件开始的计算的pos; SEEK\_CUR或者 1 则从当前位置计算; os.SEEK_END或者2则从文件尾部开始. 在unix，Windows中有效

30

[os.lstat(path)](os-lstat.html)

  
像stat(),但是没有软链接

31

[os.major(device)](os-major.html)

  
从原始的设备号中提取设备major号码 (使用stat中的st\_dev或者st\_rdev field)。

32

[os.makedev(major, minor)](os-makedev.html)

  
以major和minor设备号组成一个原始设备号

33

[os.makedirs(path\[, mode\])](os-makedirs.html)

  
递归文件夹创建函数。像mkdir(), 但创建的所有intermediate-level文件夹需要包含子文件夹。

34

[os.minor(device)](os-minor.html)

  
从原始的设备号中提取设备minor号码 (使用stat中的st\_dev或者st\_rdev field )。

35

[os.mkdir(path\[, mode\])](os-mkdir.html)

  
以数字mode的mode创建一个名为path的文件夹.默认的 mode 是 0777 (八进制)。

36

[os.mkfifo(path\[, mode\])](os-mkfifo.html)

  
创建命名管道，mode 为数字，默认为 0666 (八进制)

37

[os.mknod(filename\[, mode=0600, device\])](os-mknod.html)  
创建一个名为filename文件系统节点（文件，设备特别文件或者命名pipe）。

38

[os.open(file, flags\[, mode\])](os-open.html)

  
打开一个文件，并且设置需要的打开选项，mode参数是可选的

39

[os.openpty()](os-openpty.html)

  
打开一个新的伪终端对。返回 pty 和 tty的文件描述符。

40

[os.pathconf(path, name)](os-pathconf.html)

  
返回相关文件的系统配置信息。

41

[os.pipe()](os-pipe.html)

  
创建一个管道. 返回一对文件描述符(r, w) 分别为读和写

42

[os.popen(command\[, mode\[, bufsize\]\])](os-popen.html)

  
从一个 command 打开一个管道

43

[os.read(fd, n)](os-read.html)

  
从文件描述符 fd 中读取最多 n 个字节，返回包含读取字节的字符串，文件描述符 fd对应文件已达到结尾, 返回一个空字符串。

44

[os.readlink(path)](os-readlink.html)

  
返回软链接所指向的文件

45

[os.remove(path)](os-remove.html)

  
删除路径为path的文件。如果path 是一个文件夹，将抛出OSError; 查看下面的rmdir()删除一个 directory。

46

[os.removedirs(path)](os-removedirs.html)

  
递归删除目录。

47

[os.rename(src, dst)](os-rename.html)

  
重命名文件或目录，从 src 到 dst

48

[os.renames(old, new)](os-renames.html)

  
递归地对目录进行更名，也可以对文件进行更名。

49

[os.rmdir(path)](os-rmdir.html)

  
删除path指定的空目录，如果目录非空，则抛出一个OSError异常。

50

[os.stat(path)](os-stat.html)

  
获取path指定的路径的信息，功能等同于C API中的stat()系统调用。

51

[os.stat\_float\_times(\[newvalue\])](os-stat_float_times.html)  
决定stat_result是否以float对象显示时间戳

52

[os.statvfs(path)](os-statvfs.html)

  
获取指定路径的文件系统统计信息

53

[os.symlink(src, dst)](os-symlink.html)

  
创建一个软链接

54

[os.tcgetpgrp(fd)](os-tcgetpgrp.html)

  
返回与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组

55

[os.tcsetpgrp(fd, pg)](os-tcsetpgrp.html)

  
设置与终端fd（一个由os.open()返回的打开的文件描述符）关联的进程组为pg。

56

[os.tempnam(\[dir\[, prefix\]\])](os-tempnam.html)

  
返回唯一的路径名用于创建临时文件。

57

[os.tmpfile()](os-tmpfile.html)

  
返回一个打开的模式为(w+b)的文件对象 .这文件对象没有文件夹入口，没有文件描述符，将会自动删除。

58

[os.tmpnam()](os-tmpnam.html)

  
为创建一个临时文件返回一个唯一的路径

59

[os.ttyname(fd)](os-ttyname.html)

  
返回一个字符串，它表示与文件描述符fd 关联的终端设备。如果fd 没有与终端设备关联，则引发一个异常。

60

[os.unlink(path)](os-unlink.html)

  
删除文件路径

61

[os.utime(path, times)](os-utime.html)

  
返回指定的path文件的访问和修改的时间。

62

[os.walk(top\[, topdown=True\[, onerror=None\[, followlinks=False\]\]\])](os-walk.html)

  
输出在文件夹中的文件名通过在树中游走，向上或者向下。

63

[os.write(fd, str)](os-write.html)

  
写入字符串到文件描述符 fd中. 返回实际写入的字符串长度

### 参考地址：

*   http://kuanghy.github.io/python-os/
*   http://python.usyiyi.cn/python_278/library/os.html