python语言特点
-面向对象：以对象为中心思考问题，软件项目利于扩展和维护。
-丰富的库：库好像是汽车或家电的零件。我们不需要从头开发
一个功能，pypi网站上有十几万的项目，包括数据分析，做网站
，机器学习等领域。
=语言扩展：Python可以调用其他语言如c,c++,java编写的模块。更加
便利。俗称“胶水语言”。 
-简洁：要求强制缩进。优点代码风格统一，易于维护。可以让程序员把更
多的精力放在业务实现上。编程语言只是工具，更重要的是用工具来造东西。
编译成二进制，
-动态语言，解释型语言：计算机需要编译成二进制，
-静态语言:而Python代码先转换成一种形式，中间产物再由py 解释器来解释，缺点
是效率降低，优点代码开发效率，跨平台。
应用场景
-  爬虫           爬取网页信息
-  web网页    做网站，信息管理系统
-  后端接口
-  数据分析    大数据分析
-  科学计算     matlab 数学公式  火箭发射，水坝水流等复杂计算
-  机器学习     语言识别，图像识别
-  驱动硬件     树莓派，智能家居
-  跟其它语言项目做配合

了解其它语言
- 后端：Java Python PHP
- 前端：js nodejs
- 底层，硬件：c, c++.net
- 其它：lisp 易语言

安装Python解释器
===
##目标
安装Python解释器
##准备
1.Windows 资源管理器
显示文件后缀名和显示隐藏文件。后缀：.txt.word.py
##（了解）版本选择
Python3.7.0 
3：大版本
7：小版本
0：小版本的更新（小小版本）
我们用的是Python3大版本 平时下载注意第二位数小版本
小小版本数字尽量大
b表示bate测试版本；rc待发布版本；
版本后面什么都不加的是可供人下载的正式版本。
我们选择比较新又稳定的版本。
Windows x86表示32位。x86-64或amd64表示64位。
web-based在线安装；executable可执行安装程序 
.exe；zip 压缩包。我们选择.exe。`
最终选择为 python3.6.6-x86-
## 安装
1 打开exe
2 勾选“add python to path”,选择自定义安装.
3 optional features 全选
4 advanced option 勾选“add Python to environment variables.”
5 install 安装，成功后close对话框。

## （了解）安装目录下的文件夹的作用
-document 文档，说明书。
-library 库
-scripts 脚本
-Python.exe Python解释器的入口
-Pythonw.exe 编译

## helloworld
1 双击Python.exe 打开python交互书命令行。
命令行：非图形化得控制界面。交互式：时时运行我们键入的代码，特点
以“》》》”开头。
2 键入   print（“hello world”）   ，回车，用英文符号。


## cmd与环境变量
1 打开widows终端（cmd） 命令化比图形化界面更加底层。
win7用户 开始/附件/命令提示符；
快捷打开命令提示符 windows+r 打开运行，输入“cmd”回车 打开命令行。

##（了解）环境变量
1.windows 的环境变量 就是一些配置，系统启动时会加载这些配置。
2.环境变量里的系统变量是全局的，用户变量是个性化的。
3.环境变量有一点像桌面快捷方式，里面记录着一些路径，
每个路径中间用“；（分号）”相隔，当我们在命令行中执行一个xxx.exe程序
的时候，系统会查找这些路径，有这个程序的时候，就会调用。
4.如果Python安装时没有添加环境变量，为了使用方便需要手动添加。
5.安装完Python解释器或修改后需要重启电脑生效。（有一个不重启的环境
变量生效方法）

##windows cmd 终端与Python解释器

1 windows cmd 终端：
跟Windows操作系统有关，比如ping命令特点是“路径》”。
2 Python交互式终端：专门运行Python代码命令的。特点是“》》》”。
3 Windows终端 键盘键入“Python”进入Python终端。
4 Python终端 键入“exit()”退回到Windows终端。

##（重点）两种运行代码的方式
1 Python交互式解释器。优点：反馈快。缺点：不适合编辑大型文件。
2 在.py文件中编辑我们的代码。运行方式：“windows终端下
，“python hello.py””。优点：适合运行或编辑大型文件。



环境变量:
C:\Python36;C:\Python36\Scripts;%SystemRoot%/system32;%SystemRoot%;%SystemRoot%/System32/Wbem;C:\Program Files\MongoDB\Server\4.0.4\bin;C:\Users\Administrator\AppData\Local\Google\Chrome\Application;