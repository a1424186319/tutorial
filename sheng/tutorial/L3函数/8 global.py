#
#(老写法 a是全局变量)  从1 加到 100的和
# a = 0
# for i in range(1,101):
#    a = a + i
# print(a)

##  global（全局） 显示声明变量为全局变量
# total = 0
# def add1(n):
#     global total
#     total = total + 1
# add1()
# add1()
# add1()
# print(total)

## nonlocal（局部的）https://www.cnblogs.com/saintdingspage/p/7788958.html
def outer():
    num = 10
    def inner():
        nonlocal num
        num = 100
        print(num)
    inner()
    print(num)
outer()