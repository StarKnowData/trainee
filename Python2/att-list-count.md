Python List append()方法
======================

 [![Python 列表](../images/up.gif) Python 列表](python-lists.html)

* * *

描述
--

append() 方法用于在列表末尾添加新的对象。

语法
--

append()方法语法：
```
list.append(obj)
```
参数
--

*   obj -- 添加到列表末尾的对象。

返回值
---

该方法无返回值，但是会修改原来的列表。

实例
--

以下实例展示了 append()函数的使用方法：
```
#!/usr/bin/python

aList = \[123, 'xyz', 'zara', 'abc'\];
aList.append( 2009 );
print "Updated List : ", aList;
```
以上实例输出结果如下：
```
Updated List :  [123, 'xyz', 'zara', 'abc', 2009]
```
 [![Python 列表](../images/up.gif) Python 列表](python-lists.html)

1 篇笔记
-------

定义了两个函数一个用了extend（）方法，一个用了append（）方法
```
#!/usr/bin/python    
\# -*- coding: UTF-8 -*- 

def changeextend(str):    
    "print string with extend" mylist.extend([40,50,60]);   
    print  "print string mylist:",mylist  
    return   
def changeappend(str):  "print string with append"     mylist.append(  [7,8,9]  )   
    print  "print string mylist:",mylist   
return   
    mylist =  [10,20,30]   
    changeextend( mylist );  print  "print extend mylist:", mylist
    changeappend( mylist );    
    print  "print append mylist:", mylist 
```
输出结果：

*   print string mylist: \[10, 20, 30, 40, 50, 60\]
*   print extend mylist: \[10, 20, 30, 40, 50, 60\]
*   print string mylist: \[10, 20, 30, 40, 50, 60, \[7, 8, 9\]\]
*   print append mylist: \[10, 20, 30, 40, 50, 60, \[7, 8, 9\]\]

通过比较可知：

1.   列表可包含任何数据类型的元素，单个列表中的元素无须全为同一类型。
2.   **append()** 方法向列表的尾部添加一个新的元素。
3.   列表是以类的形式实现的。“创建”列表实际上是将一个类实例化。因此，列表有多种方法可以操作。`extend()`方法只接受一个列表作为参数，并将该参数的每个元素都添加到原有的列表中。
