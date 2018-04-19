# <h1>Python 字典(Dictionary) get()方法</h1>

<hr>
<h2>描述</h2>
<p>Python 字典(Dictionary) get() 函数返回指定键的值，如果值不在字典中返回默认值。</p>
<h2>语法</h2>
<p>get()方法语法：</p>
<pre class="prettyprint">dict.get(key, default=None)
</pre>
<h2>参数</h2>
<ul>
<li>key -- 字典中要查找的键。</li>
<li>default -- 如果指定键的值不存在时，返回该默认值值。</li>
</ul>
<h2>返回值</h2>
<p>返回指定键的值，如果值不在字典中返回默认值None。</p>
<h2>实例</h2>
<p>以下实例展示了 get()函数的使用方法：</p>


<pre class="prettyprint">#!/usr/bin/python

dict = {'Name': 'Zara', 'Age': 27}

print "Value : %s" %  dict.get('Age')
print "Value : %s" %  dict.get('Sex', "Never")
</pre>

<p>以上实例输出结果为：</p>
<pre class="prettyprint">Value : 27
Value : Never
</pre>			
		
