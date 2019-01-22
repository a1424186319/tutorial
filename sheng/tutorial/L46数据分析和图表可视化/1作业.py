# -*- coding: UTF-8 -*-
import pymysql
import jieba
from wordcloud import WordCloud
conn = pymysql.connect(host='localhost', user='root', passwd='123', db='jddb', charset='utf8')
cur = conn.cursor()
sql = """ select content from jd"""



result_list = []
cur.execute(sql)
result= cur.fetchall()
# result_list = [result]
#
# print(result_list)

for i in range(0,300):
    result_list.append(result[i])
# print(result_list)

s=''
for t in result_list:
    for e in t:
            s+=str(e)
# print(s)


# print(result)
# cur.close()
# conn.close()



results = jieba.cut(s,cut_all=False)
word_list = []
for i in results:
    print(i)
    word_list.append(i)

# print(word_list)
# print(results)

counts = {}
for word in word_list:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word, 0) + 1

items = list(counts.items())

items.sort(key=lambda x: x[1], reverse=True)
# items.sort(reverse = True)
for i in range(20):
    word, count = items[i]
    print(word,count)
#    print('{0:<10}{1:>5}'.format(word,count))

a= """手机 京东 还是 苹果 屏幕 没有 就是 感觉 速度 充电 问题 不错 可以 这个 非常 有点 特别 现在 拍照 一个"""
font = 'msyh.ttf'
wc = WordCloud(font_path=font,  # 如果是中文必须要添加这个，否则会显示成框框
               background_color='white',
               width=500,
               height=388,
               # max_font_size=300,
               min_font_size=15,
               ).generate(a)
wc.to_file('2云.png')  # 保存图片


