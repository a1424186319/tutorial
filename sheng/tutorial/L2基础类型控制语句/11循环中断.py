 #循环中断之continue

while True:
    s = input('输入：')

    if len(s) < 3:
        print('太短了，请输入3个字符以上的内容。')
        continue
    print('你输入的内容是{},长度是{},'.format(s,len(s)))

# continue:中断此次循环，但没有中断整个循环（没有跳出循环的语句块），下次循环正常运行。
# 场景：清洗数据
