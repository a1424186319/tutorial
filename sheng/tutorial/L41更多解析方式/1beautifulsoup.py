# bs包把html按照节点的层级关系转换为树形文档,然后解析,简单明了.
# 安装 beautifulsoup4   普通版本只能用于py2

from bs4 import BeautifulSoup
html = """
<html>
<body>
<a id="aaa" href="http://www.baidu.com"name="aaa" class="aaa">百度一下</a>
<a href='http://www.baidu.com'>百度一下2</a>
<h1>
多捞哦
</h1>
</body>
</html>
"""
# 实例化bs 传入参数待解析html内容和解析器.
# html.parser python内置,方便兼容性好;lxml基于c,效率较高,需要额外安装包.
bs = BeautifulSoup(html,'lxml')
bs1 = BeautifulSoup(html,'html.parser')
print(bs1)
# 漂亮的格式化输出.
# print(bs.prettify())


# 查找标签,
# print(bs.head)      #标签不存在返回None,存在返回标签

# print(bs.a)  #查找一个a标签
# print(bs.find_all('a'))     #查找所有a标签
#
# # 返回标签名称
# print(bs.name)
# print(bs.a.name)
#
# # 根据标签属性查找
# print(bs.a['href'])
#
# # (了解)删除标签属性
# print(bs.a)
# del bs.a['id']
# print(bs.a.attrs)
#
# # 标签内容
print(bs1.a.string)
#
# # 子节点和父节点
# print(bs.body.contents)    #返回列表,标签下
# print(bs.body.children)     #返回迭代器,子节
# for c in bs.body.children:
#     print(c)
# # 搜索
# print(bs.find_all('a'))
# print(bs.find_all(['a','h1']))
# # 搜索 根据属性
# print(bs.find(id="aaa"))
# # (了解)根据class
# print(bs.find_all(class_='aaa'))
# # (了解)根据class选择器语法
# print(bs.select('.aaa'))
# print(bs.select('#aaa'))
# print(bs.select('body.aaa'))

