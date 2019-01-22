# coding:utf-8
# 需求 1.封装成函数
# 2.加入代理
import requests
import json
import re
from lxml import etree
import time

# 蘑菇代理获取地址
MOGU_PROXY_URL = 'http://piping.mogumiao.com/proxy/api/get_ip_bs?appKey=fc1a46b572d54ca0a12f375eceb3b5e8&count=20&expiryDate=0&format=1&newLine=2'
FREE_PROXY_URL = 'http://192.168.221.221:5010/get/'
TIANTANG_INDEX_URL = 'http://www.ivsky.com/'
GET_PROXY_TIMEOUT = 2

def get_mogu_proxies():
    """
    请求付费代理
    :return:
    """
    try:
        resp = requests.get(MOGU_PROXY_URL)
    except Exception as e:
        print("获取代理失败", e, resp.status_code)
    if resp.status_code == 200:
        resp_dict = json.loads(resp.text)
        raw_proxies = resp_dict['msg']
        # 组装为requests包代理参数需要的格式
        res_proxies = []
        for proxy in raw_proxies:
            proxy_type = 'https'
            proxy_url = 'https://' + proxy['ip'] + proxy['port']
            res_proxies.append({proxy_type, proxy_url})
        return res_proxies

def get_free_proxies():
    """
    1.请求本地搭建的免费代理池，2.再请求要爬取的网站首页，通过则返回可用代理
    :return: {'http': 'http://xxx.xx.xx.xx:xxxx'}
    """
    i = 1
    while True:
        try:
            print('第{}次尝试获取代理'.format(i))
            resp = requests.get(FREE_PROXY_URL)
            i += 1

            proxy_url = 'http://' + resp.text
            proxies = {'http': proxy_url}
            resp2 = requests.get(TIANTANG_INDEX_URL, proxies=proxies, timeout=GET_PROXY_TIMEOUT)
        except Exception as e:
            print(e)
        else:
            if resp2.status_code == 200:
                print('可用代理', proxy_url)
                return proxies

def test_get_free_proxies():
    """
    请求百度搜索ip，检查代理ip是否生效。日志搜索“本机IP” 查看ip是否变为代理ip地址
    """
    print("开始检测代理ip可用性")
    proxies = get_free_proxies()
    try:
        response = requests.get('http://www.baidu.com/s?wd=ip', proxies=proxies, timeout=10)
        pass
    except TimeoutError:
        print("请求超时")
    except Exception as e:
        print(e)
    else:
        pattern = re.compile(r'<span class="c-gap-right">本机IP:&nbsp;.*?</span>(.*?)</td>')
        ip_address = pattern.findall(response.text)
        print('代理后的ip所在地', ip_address)

def get_album_info_list(page_no=2):
    """
    请求图集列表分页中的一页
    例如 http://www.ivsky.com/tupian/ziranfengguang/index_2.html
    获取这页的所有图集链接和名字
    :return: [('夜晚的月亮', 'https://www.tiantang.com/yueliang_vxxx'),()]
    """
    pass

# get_free_proxies()



def main():
    get_mogu_proxies()
    get_free_proxies()
    test_get_free_proxies()


if __name__=='__main__':
    main()