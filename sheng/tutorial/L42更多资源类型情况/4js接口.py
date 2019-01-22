# 4,js异步请求
# 一些后端语言框架如django是把变量渲染到html,模板最终再response返回,用户交互时需要刷新页面才能看到修改后的效果.为了更好的网页体验和前后端程序员工作分离.前端js工作中也有类似于后端requests包前端操作包.导致有些数据第一次html中并看不到.浏览器会在加载html后执行js,但requests包不会,无法直接获取到信息.
# 解决思路:js中发送http请求,浏览器开发者工具会截取到,分析http请求结构,用requests包构造请求获取信息.
"""
<html>
    <body>
        <h1>待爬取内容</h1>
        <script>
        document.onloads(
            function foo():{
            //请求商品列表
            function requests(page_no=1){resp = request('http://www.js.com/itemlist')
            dom.create('div').text = resp.text
            }
            //操作dom节点把商品信息渲染到页面中.
            })
            $.get('button').ajax({
                url:xxx,
                params:page_no = 1,
            })
        </script>
    </body>
</html>
"""
# js中
# 情况一: 类似后端的requests包,发送http请求.开发者工具中看响应是否是json数据.
# 情况二: ajax 相当于上面的封装.xml结构沟通.开发者工具XHR()
#
# 小技巧:网页请求非常多,1.排除jpg css这些请求 2.看XHR里有没有 3.看post类型
# 4.猜请求接口关键字comment list.  ctrl+F开发者工具中搜索.查看疑似请求的响应是不是json评论数据.


# 需求:爬取京东一个商品的评论.
"""
分析:https://item.jd.com/100000287113.html#askAnswer
当点击评论里的第二页的时候,url路由并没有变化没有参数.
如果django来做分页的话是下面这种方式
https://item.jd.com/100000287113.html/comment?page_no=2
其实评论信息的请求在js中,由浏览器后台执行.
所以我们需要在开发者工具中 找出js中的评论信息请求,request包构造请求,模拟浏览器的执行过程.

分析后得到的请求地址
https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv15262&productId=100000287113&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0&fold=1
然后用requests包构造这个请求.
分析参数:发现有的参数名是动态生成或不知含义或保持默认即可.考略删减具有默认值或无用的参数.

"""

import requests
import json
from lxml import etree
import csv
import pymysql

comment_url = 'https://sclub.jd.com/comment/productPageComments.action'
for i in range(0, 5):

    params = {
        'productId': 100000287113,  # 商品id,先写死 苹果手机数据库编号.
        'score': 0,
        'sortType': 5,
        'page': i,
        'pageSize': 10,
    }
    # 伪造headers.
    # cookie中有jsessionid和trackid和用户名等信息.referer和trick和用户名等信息.referer请求前的页面地址.
    headers = {
        'cookie': 'shshshfpa=b21689c6-29b6-6c6f-d664-c4fb97665a6f-1542358631; shshshfpb=1f69f9b4a232a4d98bb2de48ae40b36c4d5ba83a0f3620b425bee8668c; __jdu=1651178413; _pst=jd_4b0b6f226165b; unick=jd_4b0b6f226165b; pin=jd_4b0b6f226165b; _tp=RaeZUQtCqVD9IwjTgcKxtM4AT4Tu9lbXO84k58DZUSc%3D; user-key=e20b16d2-b9b6-4db0-98a7-e627d2eb6f83; cn=0; PCSYCityID=412; pinId=1v0AlKiHHCyTYUotUHOI47V9-x-f3wj7; ipLoc-djd=1-72-2799-0; mt_xid=V2_52007VwMVVl1YVFMaSRtsVTIAQQEPDFdGFhoZCBliARcBQVBaDkhVGgkAZ1dBAVkKAQ8YeRpdBW4fElFBW1RLH0gSXgJsARZiX2hSah1KEFUEZAoWV21bWlk%3D; unpl=V2_ZzNtbUJTQ0V1CkIDLB1dUWJUFlURAhAXc1pBU3wbDlJuBUJVclRCFXwURldnGloUZAIZWEJcQB1FCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2VHwdXAVhChddQGdzEkU4dld6HVUDYjMTbUNnAUEpDUZVch5eSGcEFl1CUUoQdQp2VUsa; __jda=122270672.1651178413.1542358629.1545914488.1545964035.10; __jdv=122270672|baidu|-|organic|not set|1545964035290; TrackID=1mOOq0sGr33Umxv2bbbFv1tTDTKFv4-Z2a36zKZ8pqe-N3IguWF9FMc_pHC3QrO58R-EybQouSqbZStAWY602urV21TRCw1jMj33jfAURxfI; shshshfp=ec7c895667e4043da9fbc1c737d98fff; __jdc=122270672; _gcl_au=1.1.1313837286.1545964385; JSESSIONID=655654A2D0E7889A833903AC6BB678B6.s1; 3AB9D23F7A4B3C9B=URTBPD7LNKOTYM6VT2QKUXUIQ7LDQVM4GBYMQD6ABC6SUEWK3CWJC54TQKFY5Q7YHJU6HE5ZHBLSVOSVMIPT3DMXEI; shshshsID=7ab311b27978b813995dc492566853c9_3_1545965745288; __jdb=122270672.9.1651178413|10.1545964035',
        'referer': 'https://item.jd.com/100000287113.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
    }

    comment_resp = requests.get(url=comment_url, params=params, headers=headers)
    # print(comment_resp.status_code)
    comment_str = comment_resp.text

    comment_dict = json.loads(comment_str)
    # commdict = json.load('4js接口.json')

    comments = comment_dict['comments']
    print(comments)

    conn = pymysql.connect(host='localhost', user='root', passwd='123', db='jddb', charset='utf8')

    for comment in comments:
        user = comment['id']
        pingjia1 = comment['content']
        shijian = comment['creationTime']
        Image = comment['referenceImage']
        Name = comment['referenceName']
        score = comment['score']
        userImage = comment['userImage']

        cur = conn.cursor()
        try:
            with conn.cursor() as cur:
                for comment in comments:
                    cursor = conn.cursor()

                    sql1 = """ select * from jduser where user = %s """ % comment['id']
                    cursor.execute(sql1)
                    rs_set = cursor.fetchone()

                    if rs_set:
                        print('这条评论已经存在')

                    insert = (
                        """INSERT INTO jduser (user,pingjia,time,Image,Name,score,userImage) VALUES(%s,%s,%s,%s,%s,%s,%s)""")

                    data = (user, pingjia1, shijian, Image, Name, score, userImage)
                    cur.execute(insert, data)
                conn.commit()
                print('第{}页成功'.format(i + 1))
                # print("成功！")
        except Exception as e:
            print(e)

    # cur.close()
    # conn.close()

    # products = comment_dict["productCommentSummary"]
    # hotComment_list = comment_dict["hotCommentTagStatistics"]

    # print('好评率:',products["goodRateShow"])
    #
    # for i in range(0, len(hotComment_list)):
    #     hot_dict = hotComment_list[i]
    #     print(hot_dict['name'])
    #     print(hot_dict["count"])

    # with open('评价.csv', mode='w', encoding='utf-8') as f:
    #     writer = csv.writer(f)
    #
    #     for comment in comments:
    #         print(comment['id'])
    # print(comment['content'])
    # pingjia = comment['content']

    # writer.writerow([pingjia])
    # print(comment['creationTime'])
    # print(comment['score'])
    # print(comment['nickname'])
    # print(comment["productColor"])
    # print(comment["productSize"])
    # print(comment["userLevelName"])
    # print('点赞数:',comment["usefulVoteCount"])
    # neicun_list = comment["productSales"]
    # for i in range(0, len(neicun_list)):
    #     neicun_dict = neicun_list[i]
    #     print('内存:',neicun_dict["saleValue"])

    # images = comment['images']
    # for image in images:
    #     print(image['imgUrl'])
