Python staticmethod() 函数
========================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

python staticmethod 返回函数的静态方法。

该方法不强制要求传递参数，如下声明一个静态方法：
```
class C(object):
    @staticmethod
    def f(arg1, arg2, ...):
        ...
```
以上实例声明了静态方法 f，类可以不用实例化就可以调用该方法 C.f()，当然也可以实例化后调用 C().f()。

### 函数语法
```
staticmethod(function)
```
参数说明：

*   无

### 实例
```
#!/usr/bin/python 
\# -*- coding: UTF-8 -*-  
class  C(object): @staticmethod  
def  f():
print('runoob'); C.f(); 
\# 静态方法无需实例化 
cobj = C()  cobj.f() 
\# 也可以实例化后调用
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)