# for i in range(10000,100000):
#     a=str(i)
#     if a[0]==a[4] and a[1]==a[3]:
#         print(a)
total = 0    #个数
for i in range(10000,100000):                            #求出来所有的5位数
    a = i // 10000                                       #万位数
    b = (i - a*10000) // 1000                            #千位数
    c = (i - a*10000 - b*1000) // 100                    #百位数
    d = (i - a*10000 - b*1000 - c*100) // 10             #十位数
    e = (i - a*10000 - b*1000 - c*100 - d*10)//1         #个位数
    if a==e and b==d:                                   #判断是否为回文数
        total += 1     #每循环一次，个数加一
        print(i)
print(total)
