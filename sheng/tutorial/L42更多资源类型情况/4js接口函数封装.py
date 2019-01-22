# 京东评论写数据库
import requests
import json
from lxml import etree
import pymysql.cursors
import time


def get_comments(product_id=None, page=None, page_size=10):
    """
    取评论
    :return: [[id,username,score,], []]或 [{'id':123123, 'username': 'zzdxyz', 'score': 5}]
    """
    comment_url = 'https://sclub.jd.com/comment/productPageComments.action'

    params = {
        'productId': product_id,  # 商品id。先写死 苹果手机。
        'score': 0,
        'sortType': 5,
        'page': page,
        'pageSize': page_size,
        # 'callback': 'fetchJSON_comment98vv15261',
        # 'isShadowSku': 0,
        # 'fold': 1
    }

    # 伪造headers。 降低被封禁的概率。
    # cookie中有jsessionid和trackid和用户名等信息。referer请求前的页面地址。useragent浏览器标识。
    headers = {
        'cookie': 'shshshfpa=c5912ac8-f696-63a4-437d-20191204d1d8-1531666020; shshshfpb=01a876290501e22aca53c7218c89142ee978ad3d34afa32745b4ada524; pinId=uGywawhW5xQ; aud=c5a66c2779ef975e95c2e6bcd122076f; aud_ver=2; __jdu=15316322076781797028717; ipLocation=%u5317%u4EAC; ipLoc-djd=1-72-2799-0; avt=3; PCSYCityID=412; pin=zzdxyz; unick=%E7%BB%86%E8%BD%AF%E8%B7%91; _tp=EtAWqzuy%2FaNSh0LFcTfGgQ%3D%3D; _pst=zzdxyz; cn=0; user-key=bb1ddddd-6808-4a0a-9ef0-486272214fae; __jdc=122270672; TrackID=12_A_Uj3VhNwy96E08U546kjQ_OUDLBz9oe6SY1cKBy1gC5rvObnItC79-lh5xLhs1PpIIwwihGx4x848lXXJlC4IZxqw1EA3ZggiJZ6bX10; thor=1206B4BD372EF4F47D5ADB6E04093C1CF85E72A62CDA84A850575F6121C961C7920737265283260552283BC968C129ACF74176D4C8098D5A2F0F4FCB9EEB1943329E4CD3624DFB217BB4783B7FC6A054B9D577B323AFE4D0AC64F3456BB34D18C1441378FB2E314B30B0C41B982FD9C11F6993C370717B280220CBF466E16BF8; ceshi3.com=000; unpl=V2_ZzNtbUdfQhUlWxJdKx0OBmJREV9KV0QTd11CVH0dCAxlBBFfclRCFX0UR1RnGF4UZwIZXEZcRhZFCEdkexhdBGMBFFpHVnMldDhFVEsRbAVjARJaQFRAFHMPQF17H1QDZgAbW0JRcyVyOHYIP0AMQzkzElhEU0EQfAxDVEsYbAViBRpcR1VCFXA4DTp6VFwBZQMVX0FUQhNyDk9UfRFaBGQKFF1EZ0Ildg%3d%3d; __jda=122270672.15316322076781797028717.1531632208.1546481134.1546481144.36; __jdb=122270672.1.15316322076781797028717|36.1546481144; __jdv=122270672|dh.tbyuantu.com|t_1000537640_|tuiguang|4901abe8a5c24c2391673d5175e83623|1546481143668; shshshfp=66ae7625488a03ea74ef89c454100a41; shshshsID=3536f0e04a4e914beb2a3be569e1cb2d_1_1546481147922',
        'referer': 'https://item.jd.com/100000287113.html',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    }

    comment_resp = requests.get(url=comment_url, params=params, headers=headers)
    print(comment_resp.status_code)
    comment_str = comment_resp.text

    comment_dict = json.loads(comment_str)
    # comment_dict = json.load('4js接口-京东评论-评论数据.json')
    comments = comment_dict['comments']

    result_list = []
    for comment in comments:
        result_list.append({
            'id': comment['id'],
            'content': comment['content'],
            'creation_time': comment['creationTime'],
            'score': comment['score'],
            'nickname': comment['nickname'],
            'product_color': comment['productColor'],
            'product_size': comment['productSize']
        })

    return result_list


def save_db(comments):
    """
    :param: comments: {list} [{'id':123123, 'content':'物美价廉东西不错', },{}]
    :return: affected_rows : {int} 成功写入的行数
    """
    connection = pymysql.connect(host='localhost', user='root', passwd='123', db='jddb', charset='utf8')
    affected_rows = 0  # 成功计数

    for comment in comments:  # 循环评论
        cursor = connection.cursor()  # 创建游标
        # 先判断一下是否已存储过

        sql1 = """ select * from jd where comment_id = %s """ % comment['id']
        cursor.execute(sql1)
        rs_set = cursor.fetchone()  # 有值返回{'id':23} 无值返回None
        if rs_set:
            print('这条评论已存在在数据库中')
            continue
        # 不存在的写入数据库
        # 写法一： 参数为列表或元组  占位符 %s
        # sql2 = """
        # insert into comment (comment_id, content, creation_time, score, nickname, product_color, product_size)
        # values (%s, %s, %s, %s, %s,   %s, %s,)
        # """
        # 注意不要在拼sql的时候通过python字符串格式化（% .formate f''）传参，应该cursor.execute(args=)传参。
        # cursor.execute(sql2, args=(comment['id'], comment['content'], ...))     # 参数为列表或元组

        # 写法二：参数为字典

        sql2 = """
        insert into jd (comment_id, content, creation_time, score, nickname, product_color, product_size)
         values (%(id)s, %(content)s, %(creation_time)s, %(score)s, %(nickname)s,   %(product_color)s, %(product_size)s)
        """
        affected_row = cursor.execute(sql2, args=comment)
        if affected_row:
            print('本条评论插入成功')
            affected_rows += affected_row

        # 写法三：批量插入，拼sql
        # 写法四：批量插入，用现成方法executemany
    connection.commit()
    connection.close()
    return affected_rows


if __name__ == '__main__':
    product_id = 100000287113  # 先写死，固定为一个商品下的评论
    page_amount = 30  # 爬取总页数，注意不要传给get_comments()函数导致每次请求固定的一页
    page_size = 10  # 每页10条评论
    time_sleep = 2

    for page in range(0, page_amount):
        comments_list = get_comments(product_id, page, page_size)
        affected_rows = save_db(comments=comments_list)
        print(f'成功写入{affected_rows}')
        print('第{}页成功'.format(page + 1))
        time.sleep(2)

    print('Done')
"""
报错：
1. id int默认4字节太短  应该bigint
2. content中有单引号导致拼出的sql错误，应该在cursor.excute
sql = 'insert into comment (comment_id, content) values (%s, %s);' % (111232, '物美价廉')
sql = 'insert into comment (comment_id, content) values ({}, {});'.format(111232, '这个商品'太好'了！')
'insert into comment (comment_id, content) values (111232, '这个商品'太好'了！');'导致报错
cursor.execute(sql)
所以参数应该在cursor.execute(sql, args=(111232, '这个商品'太好'了！'))
3. indent error 缩进错误。  怀疑sql三引号中有一个空格，换行后变为5个空格。
"""


"""
批量插入:
1.insert into coment (comment_id,content) values(111322),'这个商品"太好"了'
sql = 'insert into comment (comment_id,content)values'
for comment in comments:
    sql+='('
    sql+=comment['id']
    sql+=comment['content']
    sql+=')'
    sql+=','
    
cursor.execute(sql)
2.手动拼装比较麻烦,所以我们用现成的cursor.executemany()
sql = 'insert into comment comment_id,content) values (%s,%s)'
cursor.excutemany(sql,args=[(1123,'这个多捞哦'),(4324,'捞的嘛'),(56464,'没必要')])
"""