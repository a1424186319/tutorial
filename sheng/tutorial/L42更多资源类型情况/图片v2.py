# coding=utf-8
# 上节代码追加需求：同一图集图片放入同一文件夹下。
import requests
from lxml import etree
import os
def xia(img_set_url_list,img_set_name_list):
# 循环获取每个图集下所有缩略图
    basedir = os.path.dirname(__file__)

    for i in range(0, len(img_set_url_list)):
        print('开始本页第{}个图集'.format(i+1))
        # 当前脚本所在目录生成图集名文件夹
        if not os.path.exists(os.path.join(basedir, img_set_name_list[i])):
            # 根据图集名创建子文件夹
            os.mkdir(os.path.join(basedir, img_set_name_list[i]))
            # print('创建图集目录', os.path.join(basedir, img_set_name_list[i]))
        # 请求图集详情页  。 下面的代码跟上节课一样
        resp = requests.get(('http://www.ivsky.com' + img_set_url_list[i]))
        sub_html_content = resp.text
        sub_html_etree = etree.HTML(sub_html_content)
        # 获得图片资源src链接
        img_src_list = sub_html_etree.xpath("//ul[@class='pli']/li/div/a/img/@src")
        img_name_list = sub_html_etree.xpath("//ul[@class='pli']/li/div/a/img/@alt")
        # print(img_src_list)
        for j, img_src in enumerate(img_src_list):
            # 请求图片二进制
            print('开始下载本图集第{}张图片'.format(j))
            resp = requests.get(img_src, timeout=10)
            if not resp.status_code == 200:
                print('请求失败')
            img_bytes = resp.content
            # print(img_bytes)
            # 拼图片绝对路径，保存
            # print(os.path.join(img_set_name_list[i], f'{j}.jpg'))
            with open(os.path.join(img_set_name_list[i], f'{j}.jpg'), mode='wb') as f:
                f.write(img_bytes)
        # break   # 注释此行以爬取所有图集

def main():
    resp = requests.get('http://www.ivsky.com/tupian/ziranfengguang/index_2.html')
    if resp.status_code == 200:
        html_content = resp.content.decode()
    html_tree = etree.HTML(html_content)
    img_set_url_list = html_tree.xpath("//ul[@class='ali']/li/div/a/@href")
    img_set_name_list = html_tree.xpath("//ul[@class='ali']/li/p/a/text()")
    basedir = os.path.dirname(__file__)
    xia(img_set_url_list, img_set_name_list)


if __name__=='__main__':
    main()