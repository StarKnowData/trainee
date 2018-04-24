Python Number(数字)
=================

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
del var1\[,var2\[,var3\[....,varN\]\]\]\]
```
您可以通过使用del语句删除单个或多个对象，例如：
```
del var
del var\_a, var\_b
```
Python 支持四种不同的数值类型：

*   **整型(Int)** \- 通常被称为是整型或整数，是正或负整数，不带小数点。
*   **长整型(long integers)** \- 无限大小的整数，整数最后是一个大写或小写的L。
*   **浮点型(floating point real values)** \- 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
*   **复数(complex numbers)** \- 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。

int

long

float

complex

10

51924361L

0.0

3.14j

100

-0x19323L

15.20

45.j

-786

0122L

-21.9

9.322e-36j

080

0xDEFABCECBDAECBFBAEl

32.3+e18

.876j

-0490

535633629843L

-90.

-.6545+0J

-0x260

-052318172735L

-32.54e100

3e+26J

0x69

-4721885298529L

70.2-E12

4.53e-7j

*   长整型也可以使用小写"L"，但是还是建议您使用大写"L"，避免与数字"1"混淆。Python使用"L"来显示长整型。
*   Python还支持复数，复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型

  

* * *

Python Number 类型转换
------------------

int(x \[,base \])         将x转换为一个整数  
long(x \[,base \])        将x转换为一个长整数  
float(x )               将x转换到一个浮点数  
complex(real \[,imag \])  创建一个复数  
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

* * *

Python math 模块、cmath 模块
-----------------------

Python 中数学运算常用的函数基本都在 math 模块、cmath 模块中。

Python math 模块提供了许多对浮点数的数学运算函数。

Python cmath 模块包含了一些用于复数运算的函数。

cmath 模块的函数跟 math 模块函数基本一致，区别是 cmath 模块运算的是复数，math 模块运算的是数学运算。

要使用 math 或 cmath 函数必须先导入：

import math

查看 math 查看包中的内容:

>>\> import math
>>\> dir(math)
\['\_\_doc\_\_', '\_\_file\_\_', '\_\_loader\_\_', '\_\_name\_\_', '\_\_package\_\_', '\_\_spec\_\_', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc'\]
>>>

下文会介绍各个函数的具体应用。

查看 cmath 查看包中的内容
```
>>\> import cmath
>>\> dir(cmath)
\['\_\_doc\_\_', '\_\_file\_\_', '\_\_loader\_\_', '\_\_name\_\_', '\_\_package\_\_', '\_\_spec\_\_', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atanh', 'cos', 'cosh', 'e', 'exp', 'inf', 'infj', 'isclose', 'isfinite', 'isinf', 'isnan', 'log', 'log10', 'nan', 'nanj', 'phase', 'pi', 'polar', 'rect', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau'\]
>>>
```
实例
```
>>\> import cmath
>>\> cmath.sqrt(-1)
1j
>>\> cmath.sqrt(9)
(3+0j)
>>\> cmath.sin(1)
(0.8414709848078965+0j)
>>\> cmath.log10(100)
(2+0j)
>>>
```
* * *

Python数学函数
----------

函数

返回值 ( 描述 )

[abs(x)](func-number-abs.html)

返回数字的绝对值，如abs(-10) 返回 10

[ceil(x)](func-number-ceil.html)

返回数字的上入整数，如math.ceil(4.1) 返回 5

[cmp(x, y)](func-number-cmp.html)

如果 x < y 返回 -1, 如果 x == y 返回 0, 如果 x > y 返回 1

[exp(x)](func-number-exp.html)

返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045

[fabs(x)](func-number-fabs.html)

返回数字的绝对值，如math.fabs(-10) 返回10.0

[floor(x)](func-number-floor.html)

返回数字的下舍整数，如math.floor(4.9)返回 4

[log(x)](func-number-log.html)

如math.log(math.e)返回1.0,math.log(100,10)返回2.0

[log10(x)](func-number-log10.html)

返回以10为基数的x的对数，如math.log10(100)返回 2.0

[max(x1, x2,...)](func-number-max.html)

返回给定参数的最大值，参数可以为序列。

[min(x1, x2,...)](func-number-min.html)

返回给定参数的最小值，参数可以为序列。

[modf(x)](func-number-modf.html)

返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。

[pow(x, y)](func-number-pow.html)

x**y 运算后的值。

[round(x \[,n\])](func-number-round.html)

返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。

[sqrt(x)](func-number-sqrt.html)

返回数字x的平方根

  

* * *

Python随机数函数
-----------

随机数可以用于数学，游戏，安全等领域中，还经常被嵌入到算法中，用以提高算法效率，并提高程序的安全性。

Python包含以下常用随机数函数：

函数

描述

[choice(seq)](func-number-choice.html)

从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。

[randrange (\[start,\] stop \[,step\])](func-number-randrange.html)

从指定范围内，按指定基数递增的集合中获取一个随机数，基数缺省值为1

[random()](func-number-random.html)

随机生成下一个实数，它在\[0,1)范围内。

[seed(\[x\])](func-number-seed.html)

改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。

[shuffle(lst)](func-number-shuffle.html)

将序列的所有元素随机排序

[uniform(x, y)](func-number-uniform.html)

随机生成下一个实数，它在\[x,y\]范围内。

  

* * *

Python三角函数
----------

Python包括以下三角函数：

函数

描述

[acos(x)](func-number-acos-2.html)

返回x的反余弦弧度值。

[asin(x)](func-number-asin.html)

返回x的反正弦弧度值。

[atan(x)](func-number-atan.html)

返回x的反正切弧度值。

[atan2(y, x)](func-number-atan2.html)

返回给定的 X 及 Y 坐标值的反正切值。

[cos(x)](func-number-cos.html)

返回x的弧度的余弦值。

[hypot(x, y)](func-number-hypot.html)

返回欧几里德范数 sqrt(x\*x + y\*y)。

[sin(x)](func-number-sin.html)

返回的x弧度的正弦值。

[tan(x)](func-number-tan.html)

返回x弧度的正切值。

[degrees(x)](func-number-degrees.html)

将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0

[radians(x)](func-number-radians.html)

将角度转换为弧度

  

* * *

Python数学常量
----------

常量

描述

pi

数学常量 pi（圆周率，一般以π来表示）

e

数学常量 e，e即自然常数（自然常数）。