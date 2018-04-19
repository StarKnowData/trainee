# <h1>Python lstrip()方法</h1>
<p><a href="python-strings.html"><img class="navup" src="../images/up.gif" alt="Python 字符串"> Python 字符串</a></p>
<hr>
<h2>描述</h2>
<p>Python lstrip() 方法用于截掉字符串左边的空格或指定字符。</p>
<h2>语法</h2>
<p>lstrip()方法语法：</p>
<pre class="prettyprint">str.lstrip([chars])
</pre>
<h2>参数</h2>
<ul>
<li>chars --指定截取的字符。</li>

</ul>
<h2>返回值</h2>
<p>返回截掉字符串左边的空格或指定字符后生成的新字符串。</p>
<h2>实例</h2>
<p>以下实例展示了lstrip()的使用方法：</p>
<pre class="prettyprint">#!/usr/bin/python

str = "     this is string example....wow!!!     ";
print str.lstrip();
str = "88888888this is string example....wow!!!8888888";
print str.lstrip('8');
</pre>
<p>以上实例输出结果如下：</p>
<pre class="prettyprint">this is string example....wow!!!
this is string example....wow!!!8888888
</pre>
<hr>
<p><a href="python-strings.html"><img class="navup" src="../images/up.gif" alt="Python 字符串"> Python 字符串</a></p>			
