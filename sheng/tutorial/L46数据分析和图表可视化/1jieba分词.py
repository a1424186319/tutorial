# jieba分词
# 这个包的主要作用是把一句话,按照词汇分隔,为后面的词频统计和图片展示打基础.

import jieba
import pymysql

results = jieba.cut('把一句话 按照词汇分隔,为后面的词频统计和图片展示打基础.',cut_all=False)
word_list = []
for i in results:
    print(i)
    word_list.append(i)

for i in results:
    print('生成器只能取一次',i)

print(word_list)
print(results)




"""
生成器generator,参考第L4 5小节
跟列表相比
1.都是可迭代的,被for循环.range(0,10)返回的就是生成器.
2.generator优点用一个取一个,占内存低.
3.循环后才能看到数据不太直观:数据只能取用一次.如果想重复访问,需要再次生成generator或把数据放入变量.
"""