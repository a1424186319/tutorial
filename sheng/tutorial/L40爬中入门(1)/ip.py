import urllib.request,urllib.parse,json
origin_args = {'ip':'117.160.144.195','output':'json','ak': 'S2uzcu5og9j5h2tWPrBR9H0Fw8jiq9Wo'}
# 将中文参数base64编码
base64_args = urllib.parse.urlencode(origin_args)
# query=ATM%E6%9C%BA&region=%E9%83%91%E5%B7%9E&ak=S2uzcu5og9j5h2tWPrBR9H0Fw8jiq9Wo
base64_url = 'http://api.map.baidu.com/location/ip'
url = base64_url+'?'+base64_args
print('拼好的url',url)
resp = urllib.request.urlopen(url)
content_json = resp.read().decode()
# print(content_json)
# json转对象
content_obj = json.loads(content_json)

a = content_obj['content']['address_detail']
print(a['province'],a['city'])


