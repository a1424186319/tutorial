# User_Agent伪造(反爬)
# request_heads请求头中的一个字段,包含操作系统和浏览器信息.
# urllib requests包默认请求
# 如果来自同一个useragent的请求过于频繁,服务器有可能封掉.所以我们要伪造use_agent信息.

import random

def get_random_user_agent():
    user_agent_list = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 UBrowser/4.0.3214.0 Safari/537.36'
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
    'Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1'
    ]

    return random.choice(user_agent_list)

# print(get_random_user_agent())
# user_agent = get_random_user_agent()
# import urllib.request
# req = urllib.request.Request('https://www.baidu.com',data={'wd':'python'})
# req.add_header('User_Agent',user_agent)
# resp = urllib.request.urlopen(req)
# print(resp)
# html = resp.read().decode()
# print(html)

from fake_useragent import UserAgent
ua = UserAgent()
print(ua.random)
