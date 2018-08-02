## MySQL 基础概念

1. 数据库

2. 表 

3. 字段

4. 主键

5. 外键

## 搜索

1. 从 employees 表中搜索所有记录的 lastname，firstname，jobtitle

```sql

SELECT 
    lastname, firstname, jobtitle
FROM
    employees;

```

从****： 代表要从 **** 中搜索   FROM *****

所有的记录： 没有 where 条件

lastname： 是字段，要接到 SELECT 后面



SELECT customerName FROM customers


2. 从**表中搜索不重复的 lastname

```

SELECT DISTINCT lastname FROM ‘employees’

```


3. 从****表里搜索 lastname，firstname，jobtitle，条件是 jobtitle = ？

```


SELECT 
    lastname, firstname, jobtitle
FROM
    employees
WHERE
    jobtitle = 'Sales Rep';

```


```

SELECT 
    lastname, firstname, jobtitle
FROM
    employees
WHERE
    jobtitle = 'Sales Rep' AND officeCode = 1;


```

| 操作符         | 描述                   |
| ----------- | -------------------- |
| `=`         | 等于，几乎任何数据类型都可以使用它。   |
| `<>` 或 `!=` | 不等于                  |
| `<`         | 小于，通常使用数字和日期/时间数据类型。 |
| `>`         | 大于，                  |
| `<=`        | 小于或等于                |
| `>=`        | 大于或等于                |


3. Between and



filedA between A and B

(fieldA>=A and fieldA <=B)

4. **MySQL LIKE使用百分比(％)通配符**

假设要搜索名字以字符`a`开头的员工信息，可以在模式末尾使用百分比通配符(`％`)，如下所示：

```
SELECT 
    employeeNumber, lastName, firstName
FROM
    employees
WHERE
    firstName LIKE 'a%';
```

%  任意字符

_  一个字符

5. 


王健旭 你妹的


 - 王健旭 你妹的
 - 王健旭 你妹的%
 - %王健旭 你妹的
 - %王健旭% %你妹的%
 - %王健旭%
 - %你妹的%

6. 分页小算法


假设一个新闻系统中有21篇新闻，每一页显示5篇

 - 那么，一共多少页？21/5 = 4  21%5 = 1 4+1
 - 假如，一共20篇，那么是 4 页， 20/5 = 4 20%5 = 0 4+0
 - 假如，一共32篇，那么是 7 页， 32/5 = 6 32%5 = 2 6+1



 第一页： limit 0 , 5

 第二页： limit 5 , 5

               10,5 






  如果是第 n 页， limit   (n-1)*5，5



7. 

```

SELECT
 contactLastname,
 contactFirstname
FROM
 customers
ORDER BY
 contactLastname DESC,
 contactFirstname ASC;

```   

8. 

```

SELECT
 CONCAT_WS(', ', lastName, firstname) AS `Full name`
FROM
 employees;

```

9. 物理成绩人数>80分的人数超过10个的班级的列表


SELECT classNumber,count(*) as wuliScoreCount FROM SCOREs 

where wuliScore > 80

GROUP BY classNumber

having wuliScoreCount>10


10. 

以下查询返回在位于美国(USA)的办公室工作的员工。

SELECT 
    lastName, firstName
FROM
    employees
WHERE
    officeCode IN (SELECT 
            officeCode
        FROM
            offices
        WHERE
            country = 'USA');

SELECT 
    lastName, firstName
FROM
    employees t1
    INNER JOIN
    offices t2
    on t1.officeCode = t2.officeCode and t2.country='USA'


11. 以下查询返回最大付款额的客户。

```
SELECT 
    customerNumber, checkNumber, amount
FROM
    payments
WHERE
    amount = (SELECT 
            MAX(amount)
        FROM
            payments);
```

12. 例如，可以使用子查询找到其付款大于平均付款的客户。 首先，使用子查询来计算使用AVG聚合函数的平均付款。 然后，在外部查询中，查询大于子查询返回的平均付款的付款。参考以下查询语句的写法 -

SELECT 
    customerNumber, checkNumber, amount
FROM
    payments
WHERE
    amount > (SELECT 
            AVG(amount)
        FROM
            payments);




