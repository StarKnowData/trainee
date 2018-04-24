Python property() 函数
====================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

**property()** 函数的作用是在新式类中返回属性值。

### 语法

以下是 property() 方法的语法:
```
class property(\[fget\[, fset\[, fdel\[, doc\]\]\]\])
```
### 参数

*   fget -- 获取属性值的函数
*   fset -- 设置属性值的函数
*   fdel -- 删除属性值函数
*   doc -- 属性描述信息

### 返回值

返回新式类属性。

### 实例

定义一个可控属性值 x
-----------
```
class  C(object):
def  \_\_init\_\_(self): self._x = None 
def  getx(self):
return  self._x  
def  setx(self, value): self._x = value  
def  delx(self): 
del  self._x 
x = property(getx, setx, delx, "I'm the 'x' property.")
```
如果 _c_ 是 _C_ 的实例化, c.x 将触发 getter,c.x = value 将触发 setter ， del c.x 触发 deleter。

如果给定 doc 参数，其将成为这个属性值的 docstring，否则 property 函数就会复制 fget 函数的 docstring（如果有的话）。

将 property 函数用作装饰器可以很方便的创建只读属性：
```
class  Parrot(object): def  \_\_init\_\_(self): self._voltage = 100000 @property  def  voltage(self): """Get the current voltage."""  return  self._voltage
```
上面的代码将 voltage() 方法转化成同名只读属性的 getter 方法。
``
property 的 getter,setter 和 deleter 方法同样可以用作装饰器：

class  C(object): def  \_\_init\_\_(self): self._x = None @property  def  x(self): """I'm the 'x' property."""  return  self._x @x.setter  def  x(self, value): self._x = value @x.deleter  def  x(self): del  self._x

这个代码和第一个例子完全相同，但要注意这些额外函数的名字和 property 下的一样，例如这里的 x。

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)