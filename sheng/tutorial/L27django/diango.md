diango
===
版本:1.x和2.x不支持python2版本,只支持py3.5及以上版本.1.x路由正则风格,2.x路由风格类似flask

优点:大而全,封装多种,开箱即用.目录结构适合中大型程序.缺点,内含的功能有些用不上.

### 教程:投票应用
1.确认python版本和django版本已安装,python -m django --version
2.新建工程项目django-admin startproject mysite
3.项目目录结构,根目录下的manage.py启动服务的入口.跟项目同名的mysite文件夹下是主要项目代码.有的项目中这个文件夹又叫做app,src.    settings.py设置,urls.py路由. wsgi.py打包应用部署相关. models.pyORM相关的类,views.py业务逻辑.
4.启动项目 python manage.py runserver
5.生成应用 python manage.py startapp polls
project是项目工程,app应用是项目中一个功能模块.polls目录下migrations是sql迁移脚本,admin.py后台插件.
apps.py,models.py定义表结构的类,tests.py单元测试,views.py 业务逻辑和html渲染.

### 数据流程
浏览器请求url - mysite/urls.py - polls/views.py - 返回


### 报错
1.安装目录时报目录权限设置.解决管理员pwer


### 时间
场景:你的网站世界用户都可访问,网站上线圣诞节活动,0点到24点结束,本国人正常,外国人访问发现活动开始和结束时间提前或延后.
TIME_ZONE='UTC'
USE_TZ=TRUE
不带时区的时间aware_time,带时区的时间local_time(本地时间),
GMT,UTC(世界调和时).中国东八区,UTC+8.
python内置的datetime包生成本地时间.
如果网站只有国内访问USE_TZ设置为false,时间可以由datetime包生成,存储在数据库的不带时区的本地时间.

为了避免上面提到的场景,djiango的解决方案是.基于第三方包pytime_tz,由time_zone()生成待时区的时间.
根据time_zone设置转换utc时间存入数据库,html渲染时从取出utc时间,根据访问者的时区,在把utc转换成访问者当地的时间.
如果网站有多国访问,USE_TZ应该设置为true.

最佳实践
1.国内访问.use_tz=false time_zone='utc' datetime.now() time_zone()都行
如果网站多国访问,use_tz应该设置为true time_zone='asia/shanghai'

可能出现的错误:
前台页面时间比实际早8个小时,原因use_tz=false  time_zone='asia/shanghai'

### i18n
i18n意为国际化.网站上的菜单不同用户访问展示不同的语言.原理是有个专门关于翻译的配置文件.
