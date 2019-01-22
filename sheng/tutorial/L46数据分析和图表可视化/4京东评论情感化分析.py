# 综合项目：京东评论情感化分析
import pymysql
import jieba
from wordcloud import WordCloud

# 1 从数据库把所有用户评论查出
def get_comments():
    conn = pymysql.connect(host='localhost', user='root', passwd='123', db='jddb', charset='utf8')
    cur = conn.cursor()
    sql = """ select content from jd"""
    result_list = []
    cur.execute(sql)
    result = cur.fetchall()
    for i in range(0, 300):
        result_list.append(result[i])
    return result_list

def process_comments():
    # 所有用户评论拼成一个长字符串
    result_list = get_comments()
    s = ''
    for t in result_list:
        for e in t:
                s+=str(e)
    return s

def cut_word(s):
    # 分词 ，返回wordcloud包使用的格式
    results = jieba.cut(s, cut_all=False)
    word_list = []
    for i in results:
        # print(i)
        word_list.append(i)

    return word_list

def word_cloud(word_list):
    # 生成词云，保存到本地
    # word_list = cut_word()
    counts = {}
    for word in word_list:
        if len(word) == 1:
            continue
        else:
            counts[word] = counts.get(word, 0) + 1
    items = list(counts.items())
    items.sort(key=lambda x: x[1], reverse=True)
    # items.sort(reverse = True)
    text = ''
    for i in range(30):
        word, count = items[i]
        # print(word,count)
        # print(word)

        date = word.replace('\n',' ')
        print(date)


        # a= """手机 京东 还是 苹果 屏幕 没有 就是 感觉 速度 充电 问题 不错 可以 这个 非常 有点 特别 现在 拍照 一个"""
    # wc = WordCloud(font_path='msyh.ttf',  # 如果是中文必须要添加这个，否则会显示成框框
    #                background_color='white',
    #                width=500,
    #                height=388,
    #                # max_font_size=300,
    #                min_font_size=15,
    #                ).generate(date)
    # wc.to_file('2云.png')  # 保存图片
def gen_pei():
    # 生成饼状图
    # select  count()  group by
    # 本地生成饼状图
    pass



if __name__ == '__main__':
    a = process_comments()
    word_list = cut_word(a)
    word_cloud(word_list)