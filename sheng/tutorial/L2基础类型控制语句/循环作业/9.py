#解法一
for i in range(100,1000):
    a = i // 100
    b = (i - a*100) // 10
    c = (i - a*100 - b*10)//1
    if i == a**3 + b**3 + c**3:
        print(i)

#解法二
for x in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            i = x*100+y*10+z
            if x**3 + y**3 + z**3 == i:
                print(i)

#解法三




# 153//100
# =1
# (153 - 100*1)//10
# = 5