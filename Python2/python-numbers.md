Python  Number(数字)
==================

 Python Number 数据类型用于存储数值。

 数据类型是不允许改变的,这就意味着如果改变 Number 数据类型的值，将重新分配内存空间。

 以下实例在变量赋值时 Number 对象将被创建：

 
```

var1 = 1
var2 = 10

```

 您也可以使用del语句删除一些 Number 对象引用。 

 del语句的语法是：

 
```

del var1[,var2[,var3[....,varN]]]]

```

 您可以通过使用del语句删除单个或多个对象，例如：

 
```

del var
del var_a, var_b

```

 Python 支持四种不同的数值类型：

  * **整型(Int)** - 通常被称为是整型或整数，是正或负整数，不带小数点。
 * **长整型(long integers)** - 无限大小的整数，整数最后是一个大写或小写的L。
 * **浮点型(floating point real values)** - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
 * **复数(complex numbers)** - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。
  
<table>


</table>

<table>
<tbody><tr><th>int</th><th>long</th><th>float</th><th>complex</th></tr>
<tr><td>10</td><td>51924361L</td><td>0.0</td><td>3.14j</td></tr>
<tr><td>100</td><td>-0x19323L</td><td>15.20</td><td>45.j</td></tr>
<tr><td>-786</td><td>0122L</td><td>-21.9</td><td>9.322e-36j</td></tr>
<tr><td>080</td><td>0xDEFABCECBDAECBFBAEl</td><td>32.3+e18</td><td>.876j</td></tr>
<tr><td>-0490</td><td>535633629843L</td><td>-90.</td><td>-.6545+0J</td></tr>
<tr><td>-0x260</td><td>-052318172735L</td><td>-32.54e100</td><td>3e+26J</td></tr>
<tr><td>0x69</td><td>-4721885298529L</td><td>70.2-E12</td><td>4.53e-7j</td></tr>
</tbody>
</table>
  * 长整型也可以使用小写"L"，但是还是建议您使用大写"L"，避免与数字"1"混淆。Python使用"L"来显示长整型。
 * Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型 
    
 Python Number 类型转换
------------------

 
```

int(x [,base ])         将x转换为一个整数  
long(x [,base ])        将x转换为一个长整数  
float(x )               将x转换到一个浮点数  
complex(real [,imag ])  创建一个复数  
str(x )                 将对象 x 转换为字符串  
repr(x )                将对象 x 转换为表达式字符串  
eval(str )              用来计算在字符串中的有效Python表达式,并返回一个对象  
tuple(s )               将序列 s 转换为一个元组  
list(s )                将序列 s 转换为一个列表  
chr(x )                 将一个整数转换为一个字符  
unichr(x )              将一个整数转换为Unicode字符  
ord(x )                 将一个字符转换为它的整数值  
hex(x )                 将一个整数转换为一个十六进制字符串  
oct(x )                 将一个整数转换为一个八进制字符串  

```

  Python math 模块、cmath 模块
-----------------------

 Python 中数学运算常用的函数基本都在 math 模块、cmath 模块中。

 Python math 模块提供了许多对浮点数的数学运算函数。

 Python cmath 模块包含了一些用于复数运算的函数。

 cmath 模块的函数跟 math 模块函数基本一致，区别是 cmath 模块运算的是复数，math 模块运算的是数学运算。

 要使用 math 或 cmath 函数必须先导入：

 
```
import math
```

 查看 math 查看包中的内容:

 
```
>>> import math
>>> dir(math)
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']
>>>
```

 下文会介绍各个函数的具体应用。

 查看 cmath 查看包中的内容

 
```
>>> import cmath
>>> dir(cmath)
['__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atanh', 'cos', 'cosh', 'e', 'exp', 'inf', 'infj', 'isclose', 'isfinite', 'isinf', 'isnan', 'log', 'log10', 'nan', 'nanj', 'phase', 'pi', 'polar', 'rect', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau']
>>>
```

 实例

 
```
>>> import cmath
>>> cmath.sqrt(-1)
1j
>>> cmath.sqrt(9)
(3+0j)
>>> cmath.sin(1)
(0.8414709848078965+0j)
>>> cmath.log10(100)
(2+0j)
>>>
```

  Python数学函数
----------

 
<table>


</table>

<table>
<tbody><tr>
<th>函数</th><th>返回值 ( 描述 )</th></tr>
<tr><td><a href="func-number-abs.html" target="_blank">abs(x)</a></td><td>返回数字的绝对值，如abs(-10) 返回 10</td></tr>
<tr><td><a href="func-number-ceil.html" target="_blank">ceil(x) </a></td><td>返回数字的上入整数，如math.ceil(4.1) 返回 5</td></tr>
<tr><td><a href="func-number-cmp.html" target="_blank">cmp(x, y)</a></td><td> 如果 x &lt; y 返回 -1, 如果  x == y 返回 0,  如果 x &gt; y 返回 1</td></tr>
<tr><td><a href="func-number-exp.html" target="_blank">exp(x) </a></td><td>返回e的x次幂(e<sup>x</sup>),如math.exp(1) 返回2.718281828459045</td></tr>
<tr><td><a href="func-number-fabs.html" target="_blank">fabs(x)</a></td><td>返回数字的绝对值，如math.fabs(-10) 返回10.0</td></tr>
<tr><td><a href="func-number-floor.html" target="_blank">floor(x) </a></td><td>返回数字的下舍整数，如math.floor(4.9)返回 4</td></tr>
<tr><td><a href="func-number-log.html" target="_blank">log(x) </a></td><td>如math.log(math.e)返回1.0,math.log(100,10)返回2.0</td></tr>
<tr><td><a href="func-number-log10.html" target="_blank">log10(x) </a></td><td>返回以10为基数的x的对数，如math.log10(100)返回 2.0</td></tr>
<tr><td><a href="func-number-max.html" target="_blank">max(x1, x2,...) </a></td><td>返回给定参数的最大值，参数可以为序列。</td></tr>
<tr><td><a href="func-number-min.html" target="_blank">min(x1, x2,...) </a></td><td>返回给定参数的最小值，参数可以为序列。</td></tr>
<tr><td><a href="func-number-modf.html" target="_blank">modf(x) </a></td><td>返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。</td></tr>
<tr><td><a href="func-number-pow.html" target="_blank">pow(x, y)</a></td><td> x**y 运算后的值。</td></tr>
<tr><td><a href="func-number-round.html" target="_blank">round(x [,n])</a></td><td>返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。</td></tr>
<tr><td><a href="func-number-sqrt.html" target="_blank">sqrt(x) </a></td><td>返回数字x的平方根</td></tr>
</tbody>
</table>
   
 Python随机数函数
-----------

 随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。

 Python包含以下常用随机数函数：

 
<table>


</table>

<table>
<tbody><tr>
<th>函数</th><th>描述</th></tr>
<tr><td><a href="func-number-choice.html" target="_blank">choice(seq)</a></td><td>从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。</td></tr>
<tr><td><a href="func-number-randrange.html" target="_blank">randrange ([start,] stop [,step]) </a></td><td>从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1</td></tr>
<tr><td><a href="func-number-random.html" target="_blank">random() </a></td><td> 随机生成下一个实数，它在[0,1)范围内。</td></tr>
<tr><td><a href="func-number-seed.html" target="_blank">seed([x]) </a></td><td>改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。</td></tr>
<tr><td><a href="func-number-shuffle.html" target="_blank">shuffle(lst) </a></td><td>将序列的所有元素随机排序</td></tr>
<tr><td><a href="func-number-uniform.html" target="_blank">uniform(x, y)</a></td><td>随机生成下一个实数，它在[x,y]范围内。</td></tr>
</tbody>
</table>
   
 Python三角函数
----------

  Python包括以下三角函数：

 
<table>


</table>

<table>
<tbody><tr>
<th>函数</th><th>描述</th></tr>
<tr><td><a href="func-number-acos-2.html" target="_blank">acos(x)</a></td><td>返回x的反余弦弧度值。</td></tr>
<tr><td><a href="func-number-asin.html" target="_blank">asin(x)</a></td><td>返回x的反正弦弧度值。</td></tr>
<tr><td><a href="func-number-atan.html" target="_blank">atan(x)</a></td><td>返回x的反正切弧度值。</td></tr>
<tr><td><a href="func-number-atan2.html" target="_blank">atan2(y, x)</a></td><td>返回给定的 X 及 Y 坐标值的反正切值。</td></tr>
<tr><td><a href="func-number-cos.html" target="_blank">cos(x)</a></td><td>返回x的弧度的余弦值。</td></tr>
<tr><td><a href="func-number-hypot.html" target="_blank">hypot(x, y)</a></td><td>返回欧几里德范数 sqrt(x*x + y*y)。 </td></tr>
<tr><td><a href="func-number-sin.html" target="_blank">sin(x)</a></td><td>返回的x弧度的正弦值。</td></tr>
<tr><td><a href="func-number-tan.html" target="_blank">tan(x)</a></td><td>返回x弧度的正切值。</td></tr>
<tr><td><a href="func-number-degrees.html" target="_blank">degrees(x)</a></td><td>将弧度转换为角度,如degrees(math.pi/2) ，  返回90.0</td></tr>
<tr><td><a href="func-number-radians.html" target="_blank">radians(x)</a></td><td>将角度转换为弧度</td></tr>
</tbody>
</table>
   
 Python数学常量
----------

 
<table>


</table>

<table>
<tbody><tr>
<th>常量</th><th>描述</th></tr>
<tr><td>pi</td><td>数学常量 pi（圆周率，一般以π来表示）</td></tr>
<tr><td>e</td><td>数学常量 e，e即自然常数（自然常数）。</td></tr>
</tbody>
</table>


