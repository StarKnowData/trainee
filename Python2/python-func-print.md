Python print() 函数
=================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

**print()** 方法用于打印输出，最常见的一个函数。

> print 在 Python3.x 是一个函数，但在 Python2.x 版本不是一个函数，只是一个关键字。

### 语法

以下是 print() 方法的语法:
```
print(*objects, sep=' ', end='\\n', file=sys.stdout)
```
### 参数

*   objects -- 复数，表示可以一次输出多个对象。输出多个对象时，需要用 , 分隔。
*   sep -- 用来间隔多个对象，默认值是一个空格。
*   end -- 用来设定以什么结尾。默认值是换行符 \\n，我们可以换成其他字符串。
*   file -- 要写入的文件对象。

### 返回值

无。

* * *

实例
--

以下展示了使用 print 函数的实例：
```
Python3 下测试
-----------

>>>print(1)  1 
>>\> print("Hello World")  Hello  World 
>>\> a = 1 
>>\> b = 'runoob' 
>>\> print(a,b)  1  runoob >>\> print("aaa""bbb")  aaabbb 
>>\> print("aaa","bbb")  aaa  bbb 
>>> 
>>\> print("www","runoob","com",sep=".") 
\# 设置间隔符  
www.runoob.com
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)