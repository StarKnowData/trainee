Python 字典(Dictionary) update()方法
================================

* * *

描述
--

Python 字典(Dictionary) update() 函数把字典dict2的键/值对更新到dict里。

语法
--

update()方法语法：
```
dict.update(dict2)
```
参数
--

*   dict2 -- 添加到指定字典dict里的字典。

返回值
---

该方法没有任何返回值。

实例
--

以下实例展示了 update()函数的使用方法：
```
#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 7}
dict2 = {'Sex': 'female' }

dict.update(dict2)
print "Value : %s" %  dict
```
以上实例输出结果为：
```
Value : {'Age': 7, 'Name': 'Zara', 'Sex': 'female'}
```
