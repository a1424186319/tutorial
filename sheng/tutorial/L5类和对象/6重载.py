# 了解  重载
# 面试题：重写跟重载的区别
# 重写参考  L5/类的继承2.py一节

# 引题1：写几个关于比大小的函数
# 1> 给定两个数，返回较大的数
# 2> 给定三个数，返回最大的数
# 3> 传入数字组成的列表[1,0，-1,3.5]，返回最大的数
# 1
# def bijiao(a,b):
#     if a  >=  b:
#         print(a)
#     elif b > a:
#         print(b)
#     else:
#         print(a,b)
# bijiao(1,2)

# 2
# def get_max(a,b,c):
#     max_num = a
#     if b > max_num:
#         max_num = b
#     if c > max_num:
#         max_num = c
#     return max_num
# max_num = get_max(1,5,3)
# print('最大值',max_num)

# 3

# def get_max1(list1):
#     max = list1[0]
#     for index,num in enumerate(list1):
#         if num > max:
#             max = num
#     return max
# list1 = [1,0,-1,3.5]
# print(get_max1(list1))


class GetMaxNum(object):
    def get_max(num1, num2):
        max = num1
        if num2 > max:
            max = num2
        return max

    def get_max(a, b, c):
        max_num = a
        if b > max_num:
            max_num = b
        if c > max_num:
            max_num = c
        return max_num

    def get_max(list1):
        max = list1[0]
        for index, num in enumerate(list1):
            if num > max:
                max = num
        return max



print('最大值', GetMaxNum.get_max(1, 3))
print('最大值', GetMaxNum.get_max(1, 3, 5))
print('最大值', GetMaxNum.get_max([1, 0, -1, 3.5]))


"""
重写：子类重写父类中的同名方法。针对继承情况。
重载：类中有多个同名方法，参数不同，或者参数类型不同，这种情况较方法重载。针对方法参数的不同状况。

Python当中没有重载机制，Java语言中才有。同名函数重复定义，以最后的为准。因为Python是动态类型语言，传实参什么类型都接收；形参和实参可以穿可变个数的参数
"""
