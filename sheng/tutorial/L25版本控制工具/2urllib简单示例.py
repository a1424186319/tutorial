# urllib包,专门处理http请求响应的内置包.
# import urllib包下的__init__.py没写东西,import urllib写法并不会引入其它文件

import urllib.request
# from urllib.request import urlopen
response = urllib.request.urlopen('http://www.baidu.com')
# urlopen(url,data={参数一:值一,参数二:值二},timeout = 网页响应超时时间)
print(response)
# 从响应读信息
html_content = response.read()      #socketIO bufferReader 模式rb,从响应体中读网页信息二进制数据
print(html_content)     #字节类型的网页信息
print(html_content.decode(encoding='utf-8'))         #字节解码成字符串.
