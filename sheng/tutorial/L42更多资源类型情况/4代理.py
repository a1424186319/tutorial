import requests
url='http://www.baidu.com/s?wd=ip'
p = {
    "http":"http://14.118.135.10:808",
}
response = requests.get(url,proxies=p)

html_doc = str(response.content,'utf-8')
print(html_doc)
