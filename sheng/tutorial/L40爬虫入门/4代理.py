import urllib.request

# def user_proxy(proxy_addr, url):
#     proxy = urllib.request.ProxyHandler({'http': proxy_addr})
#     opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
#     urllib.request.install_opener(opener)
#     data = urllib.request.urlopen(url).read().decode('utf-8')
#     return data
#
# data = user_proxy( "163.204.243.91:8118", "http://www.baidu.com/s?wd=ip")
# print(data)
# print(len(data))

import requests

url = 'http://www.baidu.com/s?wd=ip'
proxy_dict = {
    "http": "http://14.118.135.10:808",
}

response = requests.get(url, proxies=proxy_dict)

html_doc = str(response.content, 'utf-8')
print(html_doc)
