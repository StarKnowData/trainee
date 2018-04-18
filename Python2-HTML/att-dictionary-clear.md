<h1>Python 字典(Dictionary) clear()方法</h1>
<hr>
<h2>描述</h2>
<p>Python 字典(Dictionary) clear() 函数用于删除字典内所有元素。</p>
<h2>语法</h2>
<p>clear()方法语法：</p>
<pre class="prettyprint prettyprinted" style=""><span class="pln">dict</span><span class="pun">.</span><span class="pln">clear</span><span class="pun">()</span></pre>
<h2>参数</h2>
<ul>
<li>NA。</li>

</ul>
<h2>返回值</h2>
<p>该函数没有任何返回值。</p>
<h2>实例</h2>
<p>以下实例展示了 clear()函数的使用方法：</p>


<pre class="prettyprint prettyprinted" style=""><span class="com">#!/usr/bin/python</span><span class="pln">

dict </span><span class="pun">=</span><span class="pln"> </span><span class="pun">{</span><span class="str">'Name'</span><span class="pun">:</span><span class="pln"> </span><span class="str">'Zara'</span><span class="pun">,</span><span class="pln"> </span><span class="str">'Age'</span><span class="pun">:</span><span class="pln"> </span><span class="lit">7</span><span class="pun">};</span><span class="pln">

</span><span class="kwd">print</span><span class="pln"> </span><span class="str">"Start Len : %d"</span><span class="pln"> </span><span class="pun">%</span><span class="pln">  len</span><span class="pun">(</span><span class="pln">dict</span><span class="pun">)</span><span class="pln">
dict</span><span class="pun">.</span><span class="pln">clear</span><span class="pun">()</span><span class="pln">
</span><span class="kwd">print</span><span class="pln"> </span><span class="str">"End Len : %d"</span><span class="pln"> </span><span class="pun">%</span><span class="pln">  len</span><span class="pun">(</span><span class="pln">dict</span><span class="pun">)</span></pre>

<p>以上实例输出结果为：</p>
<pre class="prettyprint prettyprinted" style=""><span class="typ">Start</span><span class="pln"> </span><span class="typ">Len</span><span class="pln"> </span><span class="pun">:</span><span class="pln"> </span><span class="lit">2</span><span class="pln">
</span><span class="typ">End</span><span class="pln"> </span><span class="typ">Len</span><span class="pln"> </span><span class="pun">:</span><span class="pln"> </span><span class="lit">0</span></pre>			
