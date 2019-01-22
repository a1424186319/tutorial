#urllib代理示例
#为了防止同一个ip频繁访问服务器被封锁,需要不断变化ip通过别人的电脑代理访问服务器.


"""
从哪找代理?
1.ip代理平台
2.网友搜索爬取得ip代理池
"""
import urllib.request
import random

# px  = [
#     ['http':'http'//'124.231.50.56:8118'']
#     ['http':'http'//'124.231.50.56:8118'']
#     ['http':'http'//'124.231.50.56:8118'']
# ]

# 设置代理操作器
p = urllib.request.ProxyHandler({'http':'116.7.176.75:8118'})
# 构建新的请求其,覆盖默认opner
o = urllib.request.build_opener(p,urllib.request.HTTPHandler)
urllib.request.install_opener(o)
# 请求百度搜索关键字ip
response = urllib.request.urlopen('http://www.baidu.com/s?wd=ip')
html_content = response.read().decode('utf-8')
# 返回结果中查找"本地ip"看是否已变更为代理ip
print(html_content)
