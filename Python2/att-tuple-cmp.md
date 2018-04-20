Python Tuple(元组) cmp()方法
========================

[![Python 元组](../images/up.gif)Python 元组](python-tuples.html)

* * *

描述
--

Python 元组 cmp() 函数用于比较两个元组元素。

语法
--

cmp()方法语法：
```
cmp(tuple1, tuple2)
```
参数
--

*   tuple1 -- 比较的元组。
*   tuple2 -- 比较的另外一个元组。

返回值
---

如果比较的元素是同类型的,则比较其值,返回结果。

如果两个元素不是同一种类型,则检查它们是否是数字。

*   如果是数字,执行必要的数字强制类型转换,然后比较。
*   如果有一方的元素是数字,则另一方的元素"大"(数字是"最小的")
*   否则,通过类型名字的字母顺序进行比较。

如果有一个列表首先到达末尾,则另一个长一点的列表"大"。

如果我们用尽了两个列表的元素而且所 有元素都是相等的,那么结果就是个平局,就是说返回一个 0。

实例
--

以下实例展示了 cmp()函数的使用方法：
```
#!/usr/bin/python

tuple1, tuple2 = (123, 'xyz'), (456, 'abc')

print cmp(tuple1, tuple2);
print cmp(tuple2, tuple1);
tuple3 = tuple2 + (786,);
print cmp(tuple2, tuple3)
tuple4 = (123, 'xyz')
print cmp(tuple1, tuple4)
```
以上实例输出结果如下：
```
-1
1
-1
0
```
[![Python 元组](../images/up.gif)Python 元组](python-tuples.html)