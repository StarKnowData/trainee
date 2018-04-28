Python \_\_import\_\_() 函数
==========================

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)


  描述
--

 **\_\_import\_\_()** 函数用于动态加载类和函数 。

 如果一个模块经常变化就可以使用 \_\_import\_\_() 来动态载入。

 语法
--

 \_\_import\_\_ 语法：

 
```

__import__(name[, globals[, locals[, fromlist[, level]]]])

```

  参数说明：

  * name -- 模块名
  返回值
---

 返回元组列表。

 实例
--

 以下实例展示了 \_\_import\_\_ 的使用方法：

  a.py 文件代码：
----------

 <pre>

#!/usr/bin/env python    
#encoding: utf-8  
import os
print ('在 a.py 文件中 %s' % id(os))
</pre>

  test.py 文件代码：
-------------

 <pre>

#!/usr/bin/env python    
#encoding: utf-8  
import sys
__import__('a') # 导入 a.py 模块
</pre>

 执行 test.py 文件，输出结果为：

 
```

在 a.py 文件中 4394716136
```

 [![Python 内置函数](../images/up.gif)
 Python 内置函数](python-built-in-functions.html)

