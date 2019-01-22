ORM
===
引题:学完pymysql后大家已经可以写学生管理系统mysql数据库版本了,类似sqlite版本.
步骤 1.设计数据库,
2.数据库图形工具中或py脚本中常见数据库表
3.开发
发现缺点:1.纸上.或画ER图,写sql,图形工具中运行sql创建表.2数据取出来之后需要声明一些变量来接收.这些变量与student类类似.重复 3.如果要修改表结构添加字段,要先在sql console运行sql添加字段,然后再回到后端项目取新添加的字段,修改业务逻辑.不断的在datagrip和pycharm切换.4.如果项目需要切换数据sqlite到mysql,配置服务器,后端调整. 5 有的人擅长python但不擅长sql语法.


### orm
ORM框架:  object relational mapping   对象关系映射.类映射数据库表.类似wtform从后端类生成前端html代码,orm框架会从类生成sql并执行.查询时不需要写sql直接通过类对象,只需要维护后端python代码,思维专注.
知名orm框架: sqlAlchemy(重) , django中集成的orm,peewee(轻量).