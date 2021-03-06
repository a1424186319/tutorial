#(爬虫 django)
# 给你一个网站的源代码,要求把网址都选出来,返回列表.''.find()可以做但麻烦.如果需求复杂find不能胜任正则: re regex. 专业做字符串查找筛选.比'',find() 强大的多.有自己的专用的语法.优点:功能最为强大.
# 缺点:学习曲线陡峭
# 场景:爬虫,网页解析.匹配:flask django框架的路由就是基于正则的.
# regex 三方包,功能比内置的re包更强大.
# 前缀r,raw原始字符串,运行中不需要转义字符
import re
# find 方法
html = r'<html><body><h1>hello world</h1></body></html>'
start_index = html.find('<h1>')
end_index = html.find('</h1>')
print(html[start_index:end_index+1])

# 1 匹配固定字符串1次
key = r'javapythonsld'
pattern1 = re.compile(r'python')
matcher1 = re.search(pattern1,key)
print(matcher1[0])

# re.compile 正则规则 返回包含规则的匹配器对象
# re.search(匹配器对象,待查找字符串)

# 2 任意字符串
key2 = r'<h1>hello world</h1>'
pattern2 = re.compile(r'<h1>.+</h1>')
matcher2 = re.search(pattern2,key2)
print(matcher2[0])

# 3 匹配 点 加号
key3 = r'1424186319@qq.com'
p3 = re.compile(r'.+@qq\.com')      #判断用户输入是否qq邮箱,.+不太准确
m3 = re.search(p3,key3)
print(m3[0])

# 4
key4 = r'http://www.baidu.com https://www.baidu.com'
p4 = re.compile(r'https*://')
m4 = re.search(p4,key4)
matcher4 = p4.findall(key4)
print(matcher4)

# 5 [aA] 匹配一个字符 中括号里任意一个字符符合 就算匹配到
key5 = r'SeLectSELECT'       # sql大小写不敏感
p5 = r'[sS][Ee][L1][Ee][Cc][Tt]'
pattern5 = re.compile(p5)
print(pattern5.findall(key5))

# 6 排除
key6 = r'mat cat hat pat'
p6 = re.compile(r'[^p]at')
print(p6.findall(key6))

#  7
key7 = r'1424186319@163.com.cn'  #截取出邮箱
p7 = re.compile(r'.+@.+\.')
print(p7.findall(key7))

# 8  惰性匹配
p8 = re.compile(r'.+@.+?\.')
print(p8.findall(key7))

# 9 固定次数
key9 = r'saas and sas and saaas'
p9 = re.compile(r'sa{1,2}s')
print(p9.findall(key9))

# 匹配换行后的内容  re.S
key10 = r"""aaaaahellosdaf
bbbb
world
"""
p10 = re.compile(r'hello.*?world',re.S)
print(p10.findall(key10,))

# 11 分组
key11  = r"""hello小明worldaa"""
p11  = re.compile(r'hello(.*?)world(.*?)')
print(p11.findall(key11))
