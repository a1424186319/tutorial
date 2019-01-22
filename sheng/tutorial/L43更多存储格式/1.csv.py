# csv
# csv 一种逗号分隔的简单语法的一种文件存储结构.远比数据库简单,比excel也简单.
# 场景: 备份数据,适合非电脑专业人士观看.

import csv
# 读取数据
file_path = "D:/testcsv.csv"
with open(file_path) as f:
   reader = csv.reader(f)
   result = tuple(reader)
   print(result[0][1])

# 写数据
datas = [
    ['1','小明','11'],
    ['2','憨豆','18'],
    ['3','鹏儿','88'],
]
with open('testwrite.csv',mode='w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f)
    for row in datas:
        writer.writerow(row)