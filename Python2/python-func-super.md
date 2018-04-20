Python super() 函数
=================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

**super()** 函数是用于调用父类(超类)的一个方法。

super 是用来解决多重继承问题的，直接用类名调用父类方法在使用单继承的时候没问题，但是如果使用多继承，会涉及到查找顺序（MRO）、重复调用（钻石继承）等种种问题。

MRO 就是类的方法解析顺序表, 其实也就是继承父类方法时的顺序表。

### 语法

以下是 super() 方法的语法:
```
super(type\[, object-or-type\])
```
### 参数

*   type -- 类。
*   object-or-type -- 类，一般是 self

Python3.x 和 Python2.x 的一个区别是: Python 3 可以使用直接使用 super().xxx 代替 super(Class, self).xxx :
```
Python3.x 实例：

class A:
    pass
class B(A):
    def add(self, x):
        super().add(x)

Python2.x 实例：

class A(object):   # Python2.x 记得继承 object
    pass
class B(A):
    def add(self, x):
        super(B, self).add(x)
```
### 返回值

无。

* * *

实例
--

以下展示了使用 super 函数的实例：
```
#!/usr/bin/python  
\# -*- coding: UTF-8 -*- 

class  FooParent(object):
def  \_\_init\_\_(self): self.parent = 'I\\'m the parent.'  
print  ('Parent') 
def  bar(self,message): 
print  ("%s from Parent" % message)
class  FooChild(FooParent): 
def  \_\_init\_\_(self): 
\# super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类B的对象 FooChild 转换为类 FooParent 的对象
super(FooChild,self).\_\_init\_\_() 
print  ('Child')
def  bar(self,message): super(FooChild, self).bar(message)  
print  ('Child bar fuction')  
print  (self.parent)  
if  \_\_name\_\_ == '\_\_main\_\_': 
fooChild = FooChild() 
fooChild.bar('HelloWorld')
```
执行结果：
```
Parent
Child
HelloWorld from Parent
Child bar fuction
I'm the parent.
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)