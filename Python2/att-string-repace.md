Python replace()方法
==================

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)

* * *

描述
--

Python replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次。

语法
--

replace()方法语法：
```
str.replace(old, new[, max])
```
参数
--

*   old -- 将被替换的子字符串。
*   new -- 新字符串，用于替换old子字符串。
*   max -- 可选字符串, 替换不超过 max 次

返回值
---

返回字符串中的 old（旧字符串） 替换成 new(新字符串)后生成的新字符串，如果指定第三个参数max，则替换不超过 max 次。

实例
--

以下实例展示了replace()函数的使用方法：
```
#!/usr/bin/python

str = "this is string example....wow!!! this is really string";
print str.replace("is", "was");
print str.replace("is", "was", 3);
```
以上实例输出结果如下：
```
thwas was string example....wow!!! thwas was really string
thwas was string example....wow!!! thwas is really string
```
* * *

 [![Python 字符串](../images/up.gif) Python 字符串](python-strings.html)
