# 1.练习 获取网易新闻头条部分信息
import requests
from lxml import etree

url = 'https://news.163.com'
html_content = requests.get(url).text
# print(html_content)

html = etree.HTML(html_content)
# print(html)
a = html.xpath('//div[@class="mod_top_news2"]/ul[@class="top_news_ul"]/li/a/text()')
b = html.xpath('//div[@class="mod_top_news2"]/h2/a/text()')
# for i in a:
#     print(i.xpath('text()'))
for i in a:print(i)
for n in b:print(n)






