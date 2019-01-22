# 图表
# 常见的图表:条状图,饼状图,点状分布.
# 作用和场景:1.直观整理信息,支付宝年度账单,阿里云服务器控制台,管理后台.2.好看,项目出彩.
# 常用图表包:
# 1.pillow,opencv,偏底层,是一些图表的依赖包.
# 2.matplotlib 知名的图表库,广泛应用于图表绘制和科学计算.功能完善,文档复杂.
# 3.chart.js echart,图标库最终要渲染到浏览器中,不少图标库基于js,在python web框架当中只要把数据渲染到js图表示例的响应位置,也可以使用js图表库.
# 4.pygal 后端python图标库,包含常见的图表类型,虽然种类不及matplotlib,但文档和示例非常简单.安装pip install pygal svg格式,比jpg,png复杂的一种图片格式,具备html属性,可以定义大小颜色,交互等各种功能,矢量图,体积小功能强.

import pygal
# import cairosvg
bar = pygal.Bar()
bar.add('人口(单位亿)',[11,12,12.5,13,15,16])
# bar.render_to_file('bar.svg')
bar.render_to_png('3bar.png')

