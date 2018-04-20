Python bytearray() 函数
=====================

 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)

* * *

描述
--

**bytearray()** 方法返回一个新字节数组。这个数组里的元素是可变的，并且每个元素的值范围: 0 <= x < 256。

语法
--

bytearray()方法语法：
```
class bytearray(\[source\[, encoding\[, errors\]\]\])
```
参数
--

*   如果 source 为整数，则返回一个长度为 source 的初始化数组；
*   如果 source 为字符串，则按照指定的 encoding 将字符串转换为字节序列；
*   如果 source 为可迭代类型，则元素必须为\[0 ,255\] 中的整数；
*   如果 source 为与 buffer 接口一致的对象，则此对象也可以被用于初始化 bytearray。
*   如果没有输入任何参数，默认就是初始化数组为0个元素。

返回值
---

返回新字节数组。

实例
--

以下实例展示了 bytearray() 的使用方法：
```
>>>bytearray()  bytearray(b'') >>\> bytearray(\[1,2,3\])  bytearray(b'\\x01\\x02\\x03') >>\> bytearray('runoob', 'utf-8')  bytearray(b'runoob') >>>
```
 [![Python 内置函数](../images/up.gif) Python 内置函数](python-built-in-functions.html)