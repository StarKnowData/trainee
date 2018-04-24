Python raw_input() 函数
=====================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

python raw_input() 用来获取控制台的输入。

raw_input() 将所有输入作为字符串看待，返回字符串类型。

> 注意：input() 和 raw\_input() 这两个函数均能接收 字符串 ，但 raw\_input() 直接读取控制台的输入（任何类型的输入它都可以接收）。而对于 input() ，它希望能够读取一个合法的 python 表达式，即你输入字符串的时候必须使用引号将它括起来，否则它会引发一个 SyntaxError 。
> 
> 除非对 input() 有特别需要，否则一般情况下我们都是推荐使用 raw_input() 来与用户交互。
> 
> 注意：python3 里 input() 默认接收到的是 str 类型。

### 函数语法
```
raw_input(\[prompt\])
```
参数说明：

*   prompt: 可选，字符串，可作为一个提示语。

### 实例

raw_input() 将所有输入作为字符串看待
------------------------
```
>>>a = raw_input("input:") 
input:123
>>\> type(a) <type  'str'\>
\# 字符串 
>>\> a = raw_input("input:")
input:runoob
>>\> type(a) <type  'str'\> 
\# 字符串 >>>
```
input() 需要输入 python 表达式
-----------------------
```
>>>a = input("input:") 
input:123  
\# 输入整数 
>>\> type(a) <type  'int'\> 
\# 整型
>>\> a = input("input:") 
input:"runoob" 
\# 正确，字符串表达式 
>>\> type(a) <type  'str'\>
\# 字符串 
>>\> a = input("input:") 
input:runoob
\# 报错，不是表达式 
Traceback  (most  recent  call  last): File  "<stdin>", line  1, in <module\> File  "<string>", line  1, in <module\> 
NameError: name  'runoob'  is  not  defined <type  'str'>
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)